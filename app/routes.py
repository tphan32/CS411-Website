from datetime import datetime
from app import database as db_helper
from app import app
from flask import render_template, request, redirect, session, jsonify
from flask_session import Session

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def home():
    if not session.get("username"):
        return render_template("home.html")
    return redirect("/characterSheet")
    
@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/searchHelper")
def searchHelper():
    key = request.args.get("q")
    shows = db_helper.searchDB(key)
    return jsonify(shows)

@app.route("/login", methods=["POST"])
def login():
    #TODO
    #fetch username from db
    usernameInDB = "ttp"
    passwordInDB = "12345"
    inputUserName = request.form.get("username")
    inputPassWord = request.form.get("password")
    #TODO
    #check password is correct
    if request.method == "POST" and request.form['submit_button'] == 'Login':
        if inputUserName == usernameInDB and passwordInDB == inputPassWord:
            session["username"] = inputUserName
            return redirect("/characterSheet")
        #TODO
        #print error => wrong password
    elif request.method == "POST" and request.form['submit_button'] == 'Register':
        #TODO
        #check if username is in db
        #create a new username in db
        session["username"] = inputUserName
        return redirect("/characterSheet")
    return render_template("home.html")

@app.route("/logout")
def logout():
    session["username"] = None
    return redirect("/")

@app.route("/characterSheet")
def characterSheet():
    lvl = None
    return render_template("/characterSheet.html", lvl = lvl)

@app.route("/create")
def createNewSheet():
    return render_template("/newSheet.html")

@app.route("/weapon/")
def weapon():
    try:
        items = db_helper.get_weaponName()
    except:
        items = [
            {
            "name"    : "error",
            "cost"   : "error",
            "damage"  : "error",
            "damageType": "error",
            "weight": "error",
            "propoerties": "error",
            "category": "error"
            } 
        ]
    return render_template("weapon.html", items = items)

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/query1")
def query1():
    try:
        items = db_helper.get_query_1()
    except:
        items = [
            {
                "name"    : "error",
                "level"   : "error",
                "class"  : "error",
                "SpellCastAbility": "error"
            }
        ]
    return render_template("query1.html", items = items)

@app.route("/query2/")
def query2():
    try:
        items = db_helper.get_query_2()
    except:
        items = [
            {
                "name"    : "error",
                "price"   : "error",
                "weight"  : "error",
                "category": "error"
            }
        ]
    return render_template("query2.html", items = items)
