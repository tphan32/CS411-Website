from datetime import datetime
from re import L
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
    
# @app.route("/search")
# def search():
#     return render_template("search.html")

# @app.route("/searchHelper")
# def searchHelper():
#     key = request.args.get("q")
#     shows = db_helper.searchDB(key)
#     return jsonify(shows)

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

@app.route("/explore")
def explore():
    return render_template("/explore.html")

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
        db_helper.insert_weapon(input)
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

@app.route("/armor/")
def armor():
    try:
        items = db_helper.get_armorInfo()
    except:
        items = [
            {
            "name"    : "error",
            "cost"   : "error",
            "armorClass"  : "error",
            "strNeeded": "error",
            "stealthDisadv": "error",
            "weight": "error",
            "category": "error"
            } 
        ]
    return render_template("armor.html", items = items)

@app.route("/genitem/")
def genitem():
    try:
        items = db_helper.get_genItemInfo()
    except:
        items = [
            {
            "name"    : "error",
            "price"   : "error",
            "weight": "error",
            "category": "error"
            } 
        ]
    return render_template("genitem.html", items = items)

@app.route("/proficiency/")
def proficiency():
    try:
        items = db_helper.get_profInfo()
    except:
        items = [
            {
            "name"    : "error",
            "type"   : "error",
            "subtype": "error",
            "description": "error"
            } 
        ]
    return render_template("proficiency.html", items = items)

@app.route("/removeWeapon", methods=["POST"])
def removeWeapon():
    if request.method == "POST":
        target = request.form.get("weaponName")
        db_helper.remove_weaponName(target)
    return redirect("/weapon/") 

@app.route("/randomNewWeapon")
def randNewWeapon():
    weapons = db_helper.call_pro_rand_weapon()
    return render_template("newWeapon.html", items = weapons)

@app.route("/randomNewSpell")
def randNewSpell():
    weapons = db_helper.call_pro_rand_spell()
    return render_template("newSpell.html", items = weapons)

@app.route("/classes/")
def classes():
    try:
        items = db_helper.get_classInfo()
    except:
        items = [
            {
            "name"    : "error",
            "subclass"   : "error",
            "hitPoints"  : "error",
            "description": "error",
            "gold": "error",
            "spellCastAbility": "error"
            } 
        ]
    return render_template("classes.html", items = items)

@app.route("/backgrounds/")
def backgrounds():
    try:
        items = db_helper.get_bckgInfo()
    except:
        items = [
            {
            "name"    : "error",
            "description": "error",
            "equipment": "error"
            } 
        ]
    return render_template("backgrounds.html", items = items)

@app.route("/races/")
def races():
    try:
        items = db_helper.get_raceInfo()
    except:
        items = [
            {
            "name"    : "error",
            "subrace"   : "error",
            "abilityScoreIncrease1"  : "error",
            "abilityScoreIncrease2": "error",
            "ability1": "error",
            "ability2": "error",
            "ageRange": "error",
            "description": "error",
            "size": "error",
            "speed": "error"
            }
        ]
    return render_template("races.html", items = items)

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/profile/")
def profile():
    try:
        state = db_helper.get_account_protection(session.get("username"))
    except:
        state = False
    return render_template("profile.html", state=state)

@app.route("/accountProtection")
def accountProtection():
    state = request.args.get("q")
    db_helper.update_account_protection(session.get("username"), state)
    return "OK"

@app.route("/removeAccount")
def removeAccount():
    status = db_helper.remove_account(session.get("username"))
    if status == "success":
        session.clear()
        return redirect("/logout")
    else:
        return redirect("/profile")

@app.route("/removeSpell", methods=["POST"])
def removeSpell():
    if request.method == "POST":
        target = request.form.get("spellName")
        db_helper.remove_spell(target)
    return redirect("/spells")   

@app.route("/spells/")
def spells():
    try:
        items = db_helper.get_spellInfo()
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
        Casting_Time = request.form.get("castingTime")
        spellRange = request.form.get("spellRange")
        Components = request.form.get("components")
        Duration = request.form.get("duration")
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
                db_helper.create_character(inputUserName)
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

@app.route("/lookupDesc")
def lookupDesc():
    #https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request.args
    key = list(request.args.keys())[0]
    if key == "class":
        k = request.args['class']
        table = "Class"
        cond = "className"
    elif key == "race":
        k = request.args['race']
        print(k)
        table = "Race"
        cond = "raceName"
    elif key == "bg":
        k = request.args['bg']
        table = "Background"
        cond = "bgName"
    if '_' in k:
        k = k.replace("_"," ")       
    shows = db_helper.lookupDesc(table,cond,k)
    return jsonify(shows)

@app.route("/createCharacterStep2", methods=["POST"])
def step2():
    DNDclass = request.form.get("DNDclass")
    DNDraceString = request.form.get("DNDrace")
    DNDbackground = request.form.get("DNDbackground")
    if "_" in DNDbackground:
        session["bg"] = DNDbackground.replace("_"," ")
    else:
        session["bg"] = DNDbackground



    DNDrace = []
    part = ''
    for i in DNDraceString:  
        if i != ',':
            part += i
        else:
            DNDrace.append(part)
            part = ''
    DNDrace.append(part)

    db_helper.update_character_value("ClassLevel", DNDclass + "1", session["username"])
    db_helper.update_character_value("Background", DNDbackground, session["username"])
    db_helper.update_character_value("Race", DNDrace[0], session["username"])

    return render_template("createCharacterStep2.html", DNDclass = DNDclass, DNDrace=DNDrace, DNDbackground = DNDbackground)

@app.route("/createCharacterStep3", methods=["POST"])
def step3():
    DNDclass = request.form.get("DNDclass")
    DNDrace = request.form.get("DNDrace")
    DNDbackground = request.form.get("DNDbackground")
    


    ABSTR = request.form.get("ABSTRinput")
    ABmodSTR = request.form.get("ABSTRmodinput")
    ABDEX = request.form.get("ABDEXinput")
    ABmodDEX = request.form.get("ABDEXmodinput")
    ABCON = request.form.get("ABCONinput")
    ABmodCON = request.form.get("ABCONmodinput")
    ABINT = request.form.get("ABINTinput")
    ABmodINT = request.form.get("ABINTmodinput")
    ABWIS = request.form.get("ABWISinput")
    ABmodWIS = request.form.get("ABWISmodinput")
    ABCHA = request.form.get("ABCHAinput")
    ABmodCHA = request.form.get("ABCHAmodinput")

    db_helper.update_character_value("STR",ABSTR,session["username"])
    db_helper.update_character_value("STRmod",ABmodSTR,session["username"])
    db_helper.update_character_value("DEX",ABDEX,session["username"])
    db_helper.update_character_value("DEXmod",ABmodDEX,session["username"])
    db_helper.update_character_value("CON",ABCON,session["username"])
    db_helper.update_character_value("CONmod",ABmodCON,session["username"])
    db_helper.update_character_value("INTT",ABINT,session["username"])
    db_helper.update_character_value("INTmod",ABmodINT,session["username"])
    db_helper.update_character_value("WIS",ABWIS,session["username"])
    db_helper.update_character_value("WISmod",ABmodWIS,session["username"])
    db_helper.update_character_value("CHA",ABCHA,session["username"])
    db_helper.update_character_value("CHamod",ABmodCHA,session["username"])


    DNDBskills = db_helper.get_skills_name(session["bg"])
    DNDRskills = db_helper.get_skills_name(DNDrace)
    DNDCskills, numCskills = db_helper.get_skills_name(DNDclass)
    
    return render_template("createCharacterStep3.html", DNDclass = DNDclass, DNDrace=DNDrace, DNDbackground = DNDbackground,\
         DNDBskills = DNDBskills, DNDRskills=DNDRskills, DNDCskills=DNDCskills, numCskills=numCskills)


@app.route("/createCharacterStep4", methods=["POST"])
def step4():
    DNDclass = request.form.get("className")
    DNDrace = request.form.get("raceName")
    DNDbackground = request.form.get("backgroundName")
    DNDBlangs, numBlangs = db_helper.get_langs_name(session["bg"])
    DNDRlangs,numRlangs = db_helper.get_langs_name(DNDrace)

    bSkill1 = request.form.get("bSkill1")
    bSkill2 = request.form.get("bSkill2")
    rSkill = request.form.get("rSkill")

    Prof1 = request.form.get("Prof0")
    Prof2 = request.form.get("Prof1")
    Prof3 = request.form.get("Prof2")
    Prof4 = request.form.get("Prof3")

    skills = [bSkill1, bSkill2, rSkill, Prof1, Prof2, Prof3, Prof4]
    new_skills =[]

    for part in skills:
        if part != None and part not in new_skills:
            new_skills.append(part)
    db_helper.update_character_skills(new_skills,session["username"])

    return render_template("createCharacterStep4.html", DNDclass = DNDclass, DNDrace=DNDrace, DNDbackground = DNDbackground,\
         DNDBlangs = DNDBlangs, DNDRlangs=DNDRlangs, numBlangs=numBlangs, numRlangs=numRlangs)


@app.route("/createCharacterStep5", methods=["POST"])
def step5():
    DNDclass = request.form.get("className")
    DNDrace = request.form.get("raceName")
    DNDbackground = request.form.get("backgroundName")

    DND_equipment_options = db_helper.get_equip_options(DNDclass)
    num_options = len(DND_equipment_options)

    lang1 = request.form.get("Lang0")
    lang2 = request.form.get("Lang1")
    lang3 = request.form.get("Langr0")
    lang4 = request.form.get("Langr1")

    dirty_langs = [lang1,lang2,lang3,lang4]
    clean_langs=[]
    for lang in dirty_langs:
        if lang != None:
            clean_langs.append(lang)
    print(lang1, lang2, lang3, lang4)

    db_helper.update_character_langs(clean_langs,session["username"])

    return render_template("createCharacterStep5.html", DNDclass = DNDclass, DNDrace=DNDrace, DNDbackground = DNDbackground,\
        DND_equipment_options=DND_equipment_options, num_options=num_options)



@app.route("/createCharacterStep6", methods=["POST"])
def step6():
    DNDclass = request.form.get("className")
    DNDrace = request.form.get("raceName")
    DNDbackground = request.form.get("backgroundName")

    DND_0spell_options, DND_num_0spells = db_helper.get_spell_options(DNDclass, 0,session["username"])
    DND_1spell_options, DND_num_1spells = db_helper.get_spell_options(DNDclass, 1,session["username"])

    equip1 = request.form.get("option0")
    equip2 = request.form.get("option1")
    equip3 = request.form.get("option2")
    equip4 = request.form.get("option3")

    dirty_equip = [equip1, equip2, equip3, equip4]


    db_helper.update_character_equipment(dirty_equip,session["username"])

    return render_template("createCharacterStep6.html", DNDclass = DNDclass, DNDrace=DNDrace, DNDbackground = DNDbackground,\
        DND_0spell_options=DND_0spell_options, DND_num_0spells = DND_num_0spells, DND_1spell_options = DND_1spell_options,\
             DND_num_1spells=DND_num_1spells)


@app.route("/createCharacterStep7", methods=["POST"])
def step7():
    DNDclass = request.form.get("className")
    DNDrace = request.form.get("raceName")
    DNDbackground = request.form.get("backgroundName")

    cantrip1 = request.form.get("spell0_0")
    cantrip2 = request.form.get("spell0_1")
    cantrip3 = request.form.get("spell0_2")
    cantrip4 = request.form.get("spell0_3")
    cantrips = [cantrip1,cantrip2,cantrip3,cantrip4]

    lvl1_1 = request.form.get("spell1_0")
    lvl1_2 = request.form.get("spell1_1")
    lvl1_3 = request.form.get("spell1_2")
    lvl1_4 = request.form.get("spell1_3")
    lvl1_5 = request.form.get("spell1_4")
    lvl1_6 = request.form.get("spell1_5")
    lvl_1s = [lvl1_1,lvl1_2,lvl1_3,lvl1_4,lvl1_5,lvl1_6]

    db_helper.update_character_spells(cantrips, session["username"], 0)
    db_helper.update_character_spells(lvl_1s, session["username"], 1)

    return render_template("createCharacterStep7.html", DNDclass = DNDclass, DNDrace=DNDrace, DNDbackground = DNDbackground)


@app.route("/createCharacterStep8", methods=["POST"])
def step8():
    DNDclass = request.form.get("className")
    DNDrace = request.form.get("raceName")
    DNDbackground = request.form.get("backgroundName")

    bPTrait = db_helper.get_background_info(session["bg"], "Personality Trait")
    bIdeal = db_helper.get_background_info(session["bg"], "Ideal")
    bBond = db_helper.get_background_info(session["bg"], "Bond")
    bFlaw = db_helper.get_background_info(session["bg"], "Flaw")

    char_name = request.form.get("char_name")
    alignment = request.form.get("alignment")
    age = request.form.get("age")
    eye_color = request.form.get("eye_color")
    h_feet = request.form.get("h_feet")
    h_inches = request.form.get("h_inches")
    weight = request.form.get("weight")
    skin_color = request.form.get("skin_color")
    hair_color = request.form.get("hair_color")

    physical = [char_name, alignment, age, eye_color, h_feet, h_inches, weight, skin_color, hair_color]

    db_helper.update_character_physical(physical, session["username"])

    return render_template("createCharacterStep8.html", DNDclass = DNDclass, DNDrace=DNDrace, DNDbackground = DNDbackground,\
        bPTrait=bPTrait, bIdeal=bIdeal, bBond=bBond, bFlaw=bFlaw )

@app.route("/createCharacterStep9", methods=["POST"])
def step9():

    Trait = request.form.get("Trait")
    Ideal = request.form.get("Ideal")
    Bond = request.form.get("Bond")
    Flaw = request.form.get("Flaw")

    values = [Trait,Ideal,Bond,Flaw]
    db_helper.update_character_bInfo(values, session["username"])

    return render_template("createCharacterStep9.html")

@app.route("/createCharacterStepPDF", methods=["POST"])
def stepPDF():


    db_helper.update_character_ST(session["username"])
    db_helper.update_character_prof_mod(session["username"])
    db_helper.update_character_MISC(session["username"])
    pdffile = db_helper.fillPDF(session["username"])
    print(pdffile)
    char_info, char_info_name = db_helper.get_char_info(session["username"])
    char_num = len(char_info_name)

    return render_template("createCharacterStepPDF.html", char_info=char_info, char_info_name=char_info_name, char_num=char_num,
    pdffile=pdffile)