from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd


""" App Configuration """
# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./dbdir/test.db'

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")




@app.route("/")
@login_required
def index():
    user_cash = db.execute("SELECT cash FROM users WHERE id = :id", id = session["user_id"])
    user_cash = usd(user_cash[0]["cash"])
    final_cash = 0 #Declare the final cash for user

    #Select each symbol of user
    user_symbol = db.execute("SELECT symbol, amount FROM portfolio WHERE id= :id", id = session["user_id"])

    for user in user_symbol:
        symbol = user["symbol"]
        stock  = lookup(user["symbol"])
        amount = user["amount"]

        total  = amount * stock["price"]
        final_cash+= total

        db.execute("UPDATE portfolio SET price=:price, \
            total=:total WHERE id=:id AND symbol=:symbol", \
            price=usd(stock["price"]), \
            total=usd(total), id=session["user_id"], symbol=symbol)

    #Select current cash of user
    current_cash = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])

    # Update total cash
    final_cash += current_cash[0]["cash"]

    # Select (new) user_symbol

    user_symbol = db.execute("SELECT * FROM portfolio WHERE id= :id",\
        id = session["user_id"])

    return render_template("index.html", portfolio = user_symbol, user_cash = usd(current_cash[0]["cash"]),user_total= usd(final_cash))


#Buy Stocks
@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock."""
    if request.method == "POST": #Validate request method
        #Get values and place them into variables
        if not request.form.get("amount") or not request.form.get("symbol"):
            return apology("All Data Not Filled In")

        stocks = request.form.get("symbol").upper()
        balance = db.execute("SELECT cash FROM users where id = :id",\
            id = session["user_id"] )#select user's current balance based on session id
        balance = float(balance[0]["cash"])

        #Lookup stock
        stock = lookup(stocks)
        if not stock:   #if invalid stock symbol
            return apology("Invalid Symbol Provided")

        try:    #Get amount of of stocks trying to be bought
            amount = int(request.form.get("amount"))
            if amount <= 0:         #check to see if they're valid and positive integers
                return apology("Shares must be a positive integer",)
        except:
                return apology("Shares must only be positive integers")


        stock_price = float(stock["price"] * amount)        #total stock price
        
        if stock_price>=balance:        #Check to see if total balance is more than the current bought amount
            return apology("Can't afford to buy $%i worth of stock" % stock_price)
        else:   # insert values ('id' 'symbol' 'amount' , 'price' , 'total')
            #Update cash



            #Update History
            db.execute("INSERT INTO history(id, symbol, amount, price) \
            VALUES(:id, :symbol, :amount, :price)",\
            id = session["user_id"], symbol = stock["name"], amount=request.form.get("amount"), price=usd(stock_price))

            #If same stock has been bought, select and incriment
            user_share = db.execute("SELECT price, amount FROM portfolio where id = :id and symbol = :symbol",\
            id = session["user_id"], symbol=stock["name"])

            if not user_share:
                #Create A New Portfolio For The SYMBOL and SHARE
                db.execute("INSERT INTO portfolio(id, symbol, price, amount, total) \
                VALUES(:id, :symbol, :price, :amount, :total)", \
                id= session["user_id"], symbol=stock["name"], price=usd(stock["price"]), \
                amount=request.form.get("amount"), total=usd(stock_price))

            #If User Exists In Portfolio
            else:
                db.execute("UPDATE portfolio SET price = :price, amount = :amount, total = :total \
                WHERE id = :id and symbol = :symbol",\
                price= usd(float(stock["price"])), \
                amount = int(user_share[0]["amount"] + amount), total = usd(amount * stock["price"]), \
                id = session["user_id"], symbol = stock["name"])

            db.execute("UPDATE users SET cash = :new_cash where id = :id",\
            new_cash = float(balance - stock_price), id= session["user_id"])


    else:                               #Load through post
        return render_template("buy.html")


    # redirect user to home page
    return redirect(url_for("index"))

#Show History
@app.route("/history")
@login_required
def history():
    """Show history of transactions."""
    history = db.execute("SELECT * FROM history where id=:id", id=session["user_id"])
    return render_template("history.html", history=history)




#Login User
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        if not rows:
            return apology("User Does Not Exist")
        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


#Logout User
@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))



#Get Stock Quotations
@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    #if post method is used, and all values are submitted continue. Else apologize
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide symbol")

        quote = request.form.get("symbol").upper()
        quote = lookup(quote)

        if quote["symbol"] == request.form.get("symbol").upper():

            return render_template("quoted.html",quote = quote)
        else:
            return(apology("Invalid Information Inserted"))
    else:
        return render_template("quote.html")

#Register User
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        elif not request.form.get("password_confirm"):
            return apology("must provide password confirmation")

        elif request.form.get("password") != request.form.get("password_confirm"):
            return apology ("Passwords do not match")
    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

    #Insert database executable
    register = db.execute("INSERT INTO users(username, hash) \
        VALUES(:username, :hash)", \
        username = request.form.get("username"), \
        hash=pwd_context.hash(request.form.get("password")))

    #If user exists, return an apology
    if not register:
        return apology("Username already exist")

    # remember which user has logged in
    session["user_id"] = register


    # redirect user to home page
    return redirect(url_for("index"))


#Sell Stocks
@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""

    if request.method == "POST":
        if not request.form.get("symbol") or not request.form.get("amount"):
            return apology("Incomplete Information Provided")

        symbol = request.form.get("symbol").upper()
        stockinfo = lookup(symbol)

        if not stockinfo:
            return apology("Invalid Symbol")


        try:    #Get amount of of stocks trying to be sold
            amount = int(request.form.get("amount"))
            if amount <= 0:         #check to see if they're valid and positive integers
                return apology("Shares must be a positive integer",)
        except:
                return apology("Shares must only be positive integers")

        current_amount = db.execute("SELECT amount FROM portfolio \
        where id = :id and symbol = :symbol", \
        id = session["user_id"], symbol = symbol)

        #Check if enough stocks exist to sell
        if not current_amount or current_amount[0]["amount"] < amount:
            return apology("Not Enough Stocks Owned")


        stock_price = float(stockinfo["price"] * amount)        #total stock price


        #Update History
        db.execute("INSERT INTO history (id, symbol, amount, price) \
        VALUES (:id,:symbol,:amount,:price)",\
        id = session["user_id"], symbol = symbol, amount= -amount, price = usd(stock_price))

        new_amount = current_amount[0]["amount"] - amount #Get new share amount
        #Update Profile
        if new_amount == 0:
            #Remove from portfolio
            db.execute("DELETE FROM portfolio where id = :id and symbol = :symbol", \
            id = session["user_id"], symbol = symbol)
        else:
            #Update portfolio
            db.execute("UPDATE portfolio SET price = :price ,amount = :amount, total = :total WHERE id = :id and symbol= :symbol", \
            price = usd(stockinfo["price"]), amount = new_amount, total = usd(new_amount * stockinfo["price"]), id = session["user_id"], symbol = symbol)


        #Update user cash
        current_cash = db.execute("SELECT cash FROM users where id = :id",\
        id = session["user_id"])

        db.execute("UPDATE users set cash = :cash \
        where id = :id", \
        cash = current_cash[0]["cash"]+stock_price, id = session["user_id"])



    else:
        return render_template("sell.html")


    return redirect(url_for("index"))


#Personal Touch
#Change User's Password
@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    """Register user."""
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("password"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password_confirm"):
            return apology("must provide new password")

        elif not request.form.get("password_confirm"):
            return apology("New Password Do Not Match")

        elif request.form.get("password") != request.form.get("password_confirm"):
            return apology ("Password not same")
    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("password.html")

    #Check if current password is correct
    hash_pass  = db.execute("SELECT hash from users WHERE id = :id", id = session["user_id"])

    if not pwd_context.verify(request.form.get("password"),hash_pass[0]["hash"]):
        return(apology("Passwords do not match"))

    user_info = db.execute("SELECT hash FROM users \
        WHERE id = :id", \
        id = session["user_id"])

    # redirect user to home page
    return redirect(url_for("index"))


