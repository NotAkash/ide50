from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

from helpers import *

#  configure application
app = Flask(__name__)

#  ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response


""" App Configuration """
#  configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./dbdir/test.db'

#  configure CS50 Library to use SQLite database
db = SQL("sqlite:///passbook.db")




@app.route("/")
@login_required
def index():
    user_credentials = db.execute("SELECT * from portfolio WHERE id= :id",\
    id = session["user_id"])
    return render_template("index.html", user_credentials = user_credentials)


# Add User Information
@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    """ Add Credentials To Be Saved """
    if request.method == "POST": # Validate request method
        # Get values and place them into variables
        if not request.form.get("website") or not request.form.get("email") or not request.form.get("user") or not request.form.get("password"):    # Site Email User Pass
            return apology("All Data Not Filled In")

        has_added = db.execute("SELECT * FROM portfolio WHERE id = :id AND website = :website AND email = :email AND user=:user",\
        id = session["user_id"], website = request.form.get("website"), email = request.form.get("email"), user = request.form.get("user"))

        if not has_added:
            db.execute("INSERT INTO portfolio(id, website, email, user, pass) \
            VALUES(:id, :website, :email, :user, :password)", \
            id= session["user_id"], website= request.form.get("website"),\
            email= request.form.get("email"),\
            user= request.form.get("user"),\
            password = request.form.get("password"))

        else:
            db.execute("UPDATE portfolio SET pass = :password WHERE id=:id AND website=:website AND email=:email and user=:user",\
            password = request.form.get("password"), id = session["user_id"], website = request.form.get("website"),\
            email = request.form.get("email"), user = request.form.get("user"))


        #  redirect user to home page
        return redirect(url_for("index"))




    else:                               # Load through post
        return render_template("add.html")


# Logout User
@app.route("/logout")
def logout():
    """Log user out."""

    #  forget any user_id
    session.clear()

    #  redirect user to login form
    return redirect(url_for("login"))


# Login User
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""
    #  forget any user_id
    session.clear()

    #  if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        #  ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        #  ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        #  query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        if not rows:
            return apology("User Does Not Exist")
        #  ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        #  remember which user has logged in
        session["user_id"] = rows[0]["id"]

        #  redirect user to home page
        return redirect(url_for("index"))

    #  else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")



# Register User
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""
    if request.method == "POST":

        #  ensure username was submitted
        if not request.form.get("user"):
            return apology("Must provide username")

        #  ensure password was submitted
        elif not request.form.get("pass"):
            return apology("Must provide password")

        #  ensure password and verified password is the same
        elif request.form.get("pass") != request.form.get("confirm"):
            return apology("password doesn't match")

        #  insert the new user into users, storing the hash of the user's password
        result = db.execute("INSERT INTO users (username, hash) \
                             VALUES(:username, :hashed)", \
                             username=request.form.get("user"), \
                             hashed=pwd_context.hash(request.form.get("pass")))

        if not result:
            return apology("Username already exist")

        #  remember which user has logged in
        session["user_id"] = result

        #  redirect user to home page
        return redirect(url_for("index"))

    else:
        return render_template("register.html")



# Remove Infromation
@app.route("/remove", methods=["GET", "POST"])
@login_required
def remove():
    """Remove Account Credentials"""

    if request.method != "POST":
        return render_template("remove.html")

    if not request.form.get("website") or not request.form.get("email") or not request.form.get("user") or not request.form.get("pass"):
        return apology("Must Provide All Requested Information")

    does_exist = db.execute("SELECT * FROM portfolio WHERE id=:id AND website=:website AND email=:email AND user = :user and pass = :passwrd",\
    id = session["user_id"], website = request.form.get("website"), email = request.form.get("email"),\
    user = request.form.get("user"), passwrd = request.form.get("pass"))

    if not does_exist:
        return apology("The Information Provided For Website Does Not Exist")
    else:
        db.execute("DELETE FROM portfolio WHERE id=:id AND website=:website AND email=:email AND user=:user AND pass=:passwrd",\
        id = session["user_id"], website = request.form.get("website"), email = request.form.get("email"),\
        user = request.form.get("user"), passwrd=request.form.get("pass"))

    #  redirect user to home page
    return redirect(url_for("index"))


# Personal Touch
# Change User's Password
@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    """Register user."""
    if request.method == "POST":

        #  ensure username was submitted
        if not request.form.get("password"):
            return apology("must provide username")

        #  ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide new password")

        elif not request.form.get("password_confirm"):
            return apology("New Password Do Not Match")

        elif request.form.get("password") != request.form.get("password_confirm"):
            return apology ("Password not same")
    #  else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("password.html")

    # Check if current password is correct
    hash_pass  = db.execute("SELECT hash from users WHERE id = :id", id = session["user_id"])

    if not pwd_context.verify(request.form.get("password"),hash_pass[0]["hash"]):
        return(apology("Passwords do not match"))

    user_info = db.execute("SELECT hash FROM users \
        WHERE id = :id", \
        id = session["user_id"])

    #  redirect user to home page
    return redirect(url_for("index"))