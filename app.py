#Team Fine Pizza avrahamiB huangT linW wangD
#SoftDev1 pd2
#P00: Da Art of Storytellin'
#2019-10-28

from flask import Flask, render_template, request, session, redirect, url_for, flash
from utl import ops
import sqlite3
app = Flask(__name__)
app.secret_key = "adsfgt"

session = {}
user_id = 0
@app.route("/")
def root(): #if user is logged in, redirect to the homepage, otherwise prompt user to login or register
    if 'user' in session:
        return redirect(url_for("home"))
    else:
        return render_template("landingpage.html")

@app.route("/home")
def home(): #display home page of website
    if 'user' in session:
        return render_template(
            "homepage.html",
            user = session['user']
        )
    else:
        return redirect(url_for("root"))

@app.route("/logout")
def logout(): #logs out user, return to login/register page
    session.pop('user') #removes the user from session
    return redirect(url_for("root"))

@app.route("/login", methods = ["POST"])
def login(): #check credentials against the table and confirms if they are correct
    if (request.form['username'] == "" or request.form['password'] == ""):
        flash("ERROR! Invalid username and password")
        flash("invalid error")
        return redirect(url_for("root"))
    else:
        dbfile = "holding.db"
        db = sqlite3.connect(dbfile)
        c = db.cursor()
        command = "SELECT username FROM users WHERE username = ?;"
        listUsers = c.execute(command, request.form['username'])
        for bar in listUsers:
            getPass = "SELECT password FROM users WHERE username = ?;"
            listPass = c.execute(getPass, bar[0])
            for p in listPass:
                if request.form['password'] == p[0]:
                    session['user'] = request.form['username']
                    return redirect(url_for("home"))
                else:
                    flash("ERROR! Incorrect password")
                    flash("invalid pass")
                    return redirect(url_for("root"))

@app.route("/register", methods = ["POST"])
def register(): #adds credentials to the users table and then redirects to the homepage
    try:
        global user_id
        if (request.form['username'] == "" or request.form['password'] == ""):
            flash("ERROR! Username and password cannot be blank")
            flash("register error")
            return redirect(url_for("root"))
        else:
            dbfile = "holding.db"
            db = sqlite3.connect(dbfile)
            c = db.cursor()
            user = []
            newUser = c.execute("SELECT username FROM users WHERE username = ?;", "'" + request.form['username'] + "'")
            #for new in newUser:
            #    user.append(new)
            #print(user)
            # if (len(user) > 0):
            #     flash("Username is already taken. Please choose another one.")
            #     return redirect(url_for("root"))
            # else:
            c.execute("INSERT into users VALUES(?, ?, ?);", (user_id, request.form['username'], request.form['password']))
            session['user'] = request.form['username']
            user_id += 1
            db.commit()
            db.close()
            return redirect(url_for("home"))
    except:
        flash("ERROR! Invalid characters")
        flash("register error")
        return redirect(url_for("root"))

if __name__ == "__main__":
    app.debug = True
    app.run()
