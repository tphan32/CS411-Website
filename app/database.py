from typing import List
from app import db

def get_account_protection(username):
    conn = db.connect()
    query = "SELECT protectionOn FROM AccountProtection WHERE user_name = '{}'".format(username)
    ret = conn.execute(query).fetchall()
    conn.close()
    return ret[0][0]

def update_account_protection(username, state):
    conn = db.connect()
    query = "UPDATE AccountProtection SET protectionOn = {} WHERE user_name = '{}';".format(state, username)
    conn.execute(query)
    conn.close()

def remove_account(username):
    conn = db.connect()
    query = "DELETE FROM User WHERE user_name = '{}';".format(username)
    try:
        conn.execute(query)
        conn.close()
        return "success"
    except:
        conn.close()
        return "fail"
    

def get_weaponName():
    conn = db.connect()
    query_results = conn.execute('SELECT * FROM Weapon;').fetchall()
    conn.close()
    items = []
    for result in query_results:
        item = {
            "name"    : result[0],
            "cost"   : result[1],
            "damage"  : result[2],
            "damageType": result[3],
            "weight": result[4],
            "properties": result[5],
            "category": result[6]
        } 
        items.append(item)
    return items

def remove_weaponName(target):
    query = "DELETE FROM Weapon WHERE weaponName = '{}'".format(target)
    conn = db.connect()
    conn.execute(query)
    conn.close()

def insert_new_task(input: List[str]):
    conn = db.connect()
    query = 'Insert Into Weapon (weaponName, cost, damage, damageType, weight, properties, category) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}");'.format(
        input[0], int(input[1]), input[2], input[3], int(input[4]), input[5], input[6])
    conn.execute(query)
    conn.close()

def update_weapon(input: List[str]):
    conn = db.connect()
    query = 'UPDATE Weapon SET weaponName = "{}" WHERE weaponName = "{}";'.format(input[1], input[0])
    conn.execute(query)
    conn.close()

def get_query_1() -> dict:
    query = '''
            SELECT *
            FROM
                (SELECT Spells.name, level, classes, SpellCastAbility
                FROM Class JOIN Spells ON (Class.className = Spells.classes)
                WHERE Casting_Time = '1 reaction'

                UNION

                SELECT Spells.name, level, classes, SpellCastAbility
                FROM Class JOIN Spells ON (Class.className = Spells.classes)
                WHERE Casting_Time = '1 bonus action') AS combatNonActionSpells
                LIMIT 15;
            '''
    conn = db.connect()
    query_results = conn.execute(query).fetchall()
    conn.close()
    items = []
    for result in query_results:
        item = {
            "name"    : result[0],
            "level"   : result[1],
            "class"  : result[2],
            "SpellCastAbility": result[3]
        } 
        items.append(item)
    return items

def searchDB(key):
    conn = db.connect()
    # Use %% https://stackoverflow.com/questions/42153376/python-mysql-error-when-i-use-s-in-execute
    q = 'SELECT * FROM Weapon WHERE weaponName LIKE "{}"'.format(key+"%%") + ";"
    shows = conn.execute(q).fetchall()
    conn.close()
    items = []
    for result in shows:
        item = {
            "weaponName": result[0],
        } 
        items.append(item)
    return items
    
def get_query_2() -> dict:
    query = '''
            SELECT gi1.itemName , gi1.price, gi1.weight, gi1.category 
            FROM GeneralItem gi1 JOIN (SELECT category, MAX(price) as  maxPrice 
                                    FROM GeneralItem 
                                    WHERE category LIKE "Musical instrument" 
                                    GROUP BY category) AS ins ON (gi1.category = ins.category AND gi1.price = ins.maxPrice) 
            UNION 
            SELECT itemName, price, weight, category 
            FROM GeneralItem gi2 
            WHERE price > 1
            LIMIT 15;
            '''
    conn = db.connect()
    query_results = conn.execute(query).fetchall()
    conn.close()
    items = []
    for result in query_results:
        item = {
            "name"    : result[0],
            "price"   : result[1],
            "weight"  : result[2],
            "category": result[3]
        } 
        items.append(item)
    return items


def get_spellName():
    conn = db.connect()
    query_results = conn.execute('SELECT * FROM Spells ORDER BY level;').fetchall()
    conn.close()
    items = []
    for result in query_results:
        item = {
            "name"    : result[0],
            "level"   : result[1],
            "school"  : result[2],
            "classes": result[3],
            "Casting_Time": result[4],
            "spellRange": result[5],
            "Components": result[6],
            "Duration": result[7],
            "description": result[8]
        } 
        items.append(item)
    return items

def remove_spell(target):
    query = "DELETE FROM Spells WHERE name = '{}'".format(target)
    conn = db.connect()
    conn.execute(query)
    conn.close()


def update_spell(input: List[str]):
    conn = db.connect()
    query = 'UPDATE Spells SET name = "{}" WHERE name = "{}";'.format(input[1], input[0])
    query_results = conn.execute(query)
    conn.close()

def add_spell(input: List[str]):
    conn = db.connect()
    query = 'INSERT INTO Spells(name,level,school,classes,Casting_Time,spellRange,Components,Duration,description) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}");'.format(input[0],input[1],input[2],input[3],input[4],input[5],input[6],input[7],input[8])
    query_results = conn.execute(query)
    conn.close()

def register_user(input_user: str, input_password):
    conn = db.connect()
    user_exists = user_exist(input_user)
    if user_exists == False:
        query = 'INSERT INTO User(user_name, password) VALUES("{}","{}");'.format(input_user,input_password)
        query_results = conn.execute(query)
    conn.close()
    return True

def user_exist(input_user: str):
    conn = db.connect()
    user_exists_query = conn.execute('SELECT user_name FROM User WHERE user_name = \''+ input_user + '\';').fetchall()
    user_exists = False
    for result in user_exists_query:
        if len(result) != 0:
            user_exists = True
    conn.close()
    return user_exists

def user_login(input_user: str, input_password: str):
    password = ''
    passwords = []
    if user_exist(input_user) == True:
        conn = db.connect()
        passwords = conn.execute('SELECT password FROM User WHERE user_name = \''+ input_user + '\';').fetchall()
    if len(passwords) != 0:
        password = passwords[0][0]
    if input_password == password and password != '':
        return True
    else:
        return False
        


def get_class_name():
    conn = db.connect()
    query_results = conn.execute('SELECT className FROM Class;').fetchall()
    conn.close()
    classes = []
    for result in query_results:
        item = {
            "name"    : result[0],
        } 
        classes.append(item)
    return classes

def get_race_name():
    conn = db.connect()
    query_results = conn.execute('SELECT raceName, abilityScoreIncrease1, abilityScoreIncrease2, ability1, ability2 FROM Race;').fetchall()
    conn.close()
    races = []
    for result in query_results:
        item = {
            
            "name"    : result[0],
            "AB1" : result[1],
            "AB2" : result[2],
            "ABscore1" : result[3],
            "ABscore2" : result[4]
        } 
        races.append(item)
    print(item)
    return races


def get_background_name():
    conn = db.connect()
    query_results = conn.execute('SELECT DISTINCT source_name FROM TrainedProf WHERE source_type = \'background\';').fetchall()
    conn.close()
    backgrounds = []
    for result in query_results:
        item = {
            "name"    : result[0],
        } 
        backgrounds.append(item)
    return backgrounds
    
def get_skills_name(from_where):
    conn = db.connect()
    query_results = conn.execute('SELECT prof_Name FROM TrainedProf WHERE source_name = \''+from_where+'\' AND prof_Name in (SELECT Name from Proficiency WHERE Type = \'skill\');').fetchall()
    conn.close()
    all = []
    for result in query_results:
        item = {
            "name"    : result[0],
        }
        all.append(item)

       
    if from_where in ['Barbarian','Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Sorcerer', 'Warlock', 'Wizard']:
        return all, 2
    elif from_where == 'Ranger' or from_where == 'Bard':
        return all, 3
    elif from_where == 'Rogue':
        return all, 4

    

    return all
