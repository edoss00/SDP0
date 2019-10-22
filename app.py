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
    return render_template("landingpage.html")

@app.route("/home")
def home(): #display home page of website
    return render_template("homepage.html")

@app.route("/logout")
def logout(): #logs out user, return to login/register page
    session.pop('user') #removes the user from session
    return redirect(url_for("root"))

@app.route("/login", methods = ["POST"])
def login(): #check credentials against the table and confirms if they are correct
    return "hello"

@app.route("/register", methods = ["POST"])
def register(): #adds credentials to the users table and then redirects to the homepage
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.debug = True
    app.run()
