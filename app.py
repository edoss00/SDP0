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
    return render_template(
        "homepage.html",
        user = session['user']
    )

@app.route("/logout")
def logout(): #logs out user, return to login/register page
    session.pop('user') #removes the user from session
    return redirect(url_for("root"))

@app.route("/login", methods = ["POST"])
def login(): #check credentials against the table and confirms if they are correct
    return "hello"

@app.route("/register", methods = ["POST"])
def register(): #adds credentials to the users table and then redirects to the homepage
    global user_id
    dbfile = "holding.db"

    db = sqlite3.connect(dbfile)
    c = db.cursor()

    if (request.form['username'] == "" or request.form['password'] == ""):
        flash("ERROR! Username and password cannot be blank")
        flash("register error")
        return redirect(url_for("root"))
    else:
        c.execute(ops.insert('users', user_id, request.form['username'], request.form['password']))
        session['user'] = request.form['username']
        user_id += 1
        db.commit()
        db.close()
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.debug = True
    app.run()
