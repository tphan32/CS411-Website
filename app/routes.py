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

@app.route("/updWeapon", methods=["GET","POST"])
def update_weapon():
    input = []
    if request.method == "POST":
        old_name = request.form.get("oldname")
        new_name = request.form.get("newname")
        input.append(old_name)
        input.append(new_name)
        db_helper.update_weapon (input)
    return redirect("/weapon")

@app.route("/add", methods=["POST"])
def create():
    input = []
    if request.method == "POST":
        name = request.form.get("name")
        cost = request.form.get("cost")
        damage = request.form.get("damage")
        damageType = request.form.get("damageType")
        weight = request.form.get("weight")
        properties = request.form.get("properties")
        category = request.form.get("category")
        input.append(name)
        input.append(cost)
        input.append(damage)
        input.append(damageType)
        input.append(weight)
        input.append(properties)
        input.append(category)
        db_helper.insert_new_task(input)
    return redirect("/weapon/")

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

@app.route("/removeWeapon", methods=["POST"])
def removeWeapon():
    if request.method == "POST":
        target = request.form.get("weaponName")
        db_helper.remove_weaponName(target)
    return redirect("/weapon/") 

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




@app.route("/removeSpell", methods=["POST"])
def removeSpell():
    if request.method == "POST":
        target = request.form.get("spellName")
        db_helper.remove_spell(target)
    return redirect("/spells")   

@app.route("/spells/")
def spells():
    try:
        items = db_helper.get_spellName()
    except:
        items = [
            {
            "name"    : "error",
            "level"   : "error",
            "school"  : "error",
            "classes": "error",
            "Casting_Time": "error",
            "spellRange": "error",
            "Components": "error",
            "Duration": "error",
            "description": "error"
            } 
        ]
    return render_template("spells.html", items = items)

@app.route("/updSpell", methods=["GET","POST"])
def update_spell():
    input = []
    if request.method == "POST":
        old_name = request.form.get("oldSpellname")
        new_name = request.form.get("newSpellname")
        input.append(old_name)
        input.append(new_name)
        db_helper.update_spell(input)
    return redirect("/spells")

@app.route("/addSpell", methods=["GET","POST"])
def createSpell():
    input = []
    if request.method == "POST":
        name = request.form.get("name")
        level = request.form.get("level")
        school = request.form.get("school")
        classes = request.form.get("classes")
        Casting_Time = request.form.get("Casting_Time")
        spellRange = request.form.get("spellRange")
        Components = request.form.get("Components")
        Duration = request.form.get("Duration")
        description = request.form.get("description")
        input.append(name)
        input.append(level)
        input.append(school)
        input.append(classes)
        input.append(Casting_Time)
        input.append(spellRange)
        input.append(Components)
        input.append(Duration)
        input.append(description)
        db_helper.add_spell(input)
    return redirect("/spells")

@app.route("/login", methods=["POST"])
def login():
    inputUserName = request.form.get("username")
    inputPassWord = request.form.get("password")

    if request.method == "POST" and request.form['submit_button'] == 'Login':
        #checks if the user exists
        #checks if the login info is correct
        user_exists = db_helper.user_exist(inputUserName)
        access = db_helper.user_login(inputUserName, inputPassWord)

        #If the user exists it checks the login info
        #If login info is wrong, they go back to homepage
        #If login info is right, they go to charactersheet
        #If user does not exists, then they are taken to register

        if user_exists:
            if access:
                session["username"] = inputUserName
                return redirect("/characterSheet")
            else:
                return render_template("home.html")
        else:
            return render_template("register.html")

    if request.method == "POST" and request.form['submit_button'] == 'Register':
        
        inputUserName = request.form.get("username")
        inputPassWord = request.form.get("password")

    if db_helper.register_user(inputUserName,inputPassWord) == True:
        return render_template("home.html")
    else:
       return render_template("register.html")





@app.route("/createCharacterStep1", methods=["POST"])
def step1():
    try:
        classes = db_helper.get_class_name()
        
    except:
        classes = [
            {
            "name"    : "error",
            } 
        ]
    try:
        backgrounds = db_helper.get_background_name()

    except:
        backgrounds = [
            {
            "name"    : "error",
            } 
        ]

    try:
        races = db_helper.get_race_name()

    except:
        races = [
            {
            "name"    : "error",
            "AB1"    : "error",
            "AB2"    : "error",
            "ABscore1"    : "error",
            "ABscore2"    : "error",
            } 
        ]
        
    return render_template("createCharacterStep1.html", classes = classes, backgrounds = backgrounds, races = races)

@app.route("/createCharacterStep2", methods=["POST"])
def step2():
    DNDclass = request.form.get("DNDclass")
    DNDraceString = request.form.get("DNDrace")
    DNDbackground = request.form.get("DNDbackground")

    DNDrace = []
    part = ''
    for i in DNDraceString:  
        if i != ',':
            part += i
        else:
            DNDrace.append(part)
            part = ''
    DNDrace.append(part)


    return render_template("createCharacterStep2.html", DNDclass = DNDclass, DNDrace=DNDrace, DNDbackground = DNDbackground)

@app.route("/createCharacterStep3", methods=["POST"])
def step3():
    DNDclass = request.form.get("DNDclass")
    DNDrace = request.form.get("DNDrace")
    DNDbackground = request.form.get("DNDbackground")
    DNDBskills = db_helper.get_skills_name(DNDbackground)
    DNDRskills = db_helper.get_skills_name(DNDrace)
    DNDCskills, numCskills = db_helper.get_skills_name(DNDclass)

    return render_template("createCharacterStep3.html", DNDclass = DNDclass, DNDrace=DNDrace, DNDbackground = DNDbackground,\
         DNDBskills = DNDBskills, DNDRskills=DNDRskills, DNDCskills=DNDCskills, numCskills=numCskills)