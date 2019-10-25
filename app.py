#Team Fine Pizza avrahamiB huangT linW wangD
#SoftDev1 pd2
#P00: Da Art of Storytellin'
#2019-10-28

from flask import Flask, render_template, request, session, redirect, url_for, flash
import sqlite3
app = Flask(__name__)
app.secret_key = "adsfgt"

session = {}

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
            user = session['user'],
            storyName = getStories()
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
        command = "SELECT username FROM users WHERE username = \"{}\";"
        listUsers = c.execute(command.format(request.form['username']))
        bar = list(enumerate(listUsers))
        if len(bar) > 0:
            getPass = "SELECT password FROM users WHERE username = \"{}\";"
            listPass = c.execute(getPass.format(bar[0][1][0]))
            for p in listPass:
                if request.form['password'] == p[0]:
                    session['user'] = request.form['username']
                    return redirect(url_for("home"))
                else:
                    flash("ERROR! Incorrect password")
                    flash("invalid error")
                    return redirect(url_for("root"))
        else:
            flash("ERROR! Incorrect username")
            flash("invalid error")
            return redirect(url_for("root"))

@app.route("/register", methods = ["POST"])
def register(): #adds credentials to the users table and then redirects to the homepage
    #try:
    if (request.form['username'] == "" or request.form['password'] == ""):
        flash("ERROR! Username and password cannot be blank")
        flash("register error")
        return redirect(url_for("root"))
    else:
        dbfile = "holding.db"
        db = sqlite3.connect(dbfile)
        c = db.cursor()
        command = "SELECT username FROM users WHERE username = \"{}\";"
        newUser = c.execute(command.format(request.form['username']))
        if len(list(enumerate(newUser))) > 0:
            flash("Username is already taken. Please choose another one.")
            flash("register error")
            return redirect(url_for("root"))
        else:
            user_id = getTableLen("users")
            c.execute("INSERT into users VALUES(?, ?, ?);", (user_id, request.form['username'], request.form['password']))
            session['user'] = request.form['username']
            db.commit()
            db.close()
            return redirect(url_for("home"))
    #except:
    #    flash("ERROR! Invalid characters")
    #    flash("register error")
    #    return redirect(url_for("root"))

@app.route("/create")
def create(): #lets the user create a new story
    return render_template("newpage.html")

@app.route("/add", methods = ["POST"])
def addStory(): #checks if the story exists and registers the story if it does not yet
    dbfile = "holding.db"
    db = sqlite3.connect(dbfile)
    c = db.cursor()
    command = "SELECT story_name FROM stories WHERE story_name = \"{}\";"
    sameStory = c.execute(command.format(request.form['title']))
    if len(list(enumerate(sameStory))) > 0:
        flash("Title has already been taken. Please choose another one.")
        return redirect(url_for("create"))
    else:
        story_id = getTableLen("stories")
        command = "INSERT INTO stories VALUES(?, ?, ?, ?);"
        c.execute(command, (story_id, request.form['title'], request.form['story'], request.form['story']))
        command = "SELECT user_id FROM users WHERE username = \"{}\";"
        q = c.execute(command.format(session['user']))
        id = -1
        for bar in q:
            id = bar[0]
        command = "INSERT INTO edits VALUES(?, ?);"
        c.execute(command, (id, getTableLen("stories")))
    db.commit()
    db.close()
    return redirect(url_for("home"))

@app.route("/read/<file>")
def read(file):
    dbfile = "holding.db"
    db = sqlite3.connect(dbfile)
    c = db.cursor()
    command = "SELECT story_text FROM stories WHERE story_name = \"{}\""
    q = c.execute(command.format(file))
    text = ""
    for bar in q:
        text = bar[0]
    return render_template("readonly.html", name = file, story = text)

def has_edited(user, story):
    outline = "SELECT * FROM edits WHERE username = {} AND story_id = {};"
    command = outline.format(user, story)
    q = c.execute(command)
    for bar in q:
      return True
    return False

def getTableLen(tbl):
    dbfile = "holding.db"
    db = sqlite3.connect(dbfile)
    c = db.cursor()
    command = "SELECT * FROM {};"
    q = c.execute(command.format(tbl))
    count = 0
    for line in q:
        count += 1
    return count

def getStories():
    dbfile = "holding.db"
    db = sqlite3.connect(dbfile)
    c = db.cursor()
    command = "SELECT story_name FROM stories;"
    storyList = c.execute(command)
    list = []
    for story in storyList:
        list.append(story[0])
    db.commit()
    db.close()
    return list

if __name__ == "__main__":
    app.debug = True
    app.run()
