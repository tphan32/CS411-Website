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
    
def call_pro_rand_weapon():
    conn = db.connect()
    query = "CALL randomNewWeapon();"
    query_results = conn.execute(query).fetchall()
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
    query_results = conn.execute('SELECT className FROM Class WHERE className IN(SELECT className from ClassEquipment);').fetchall()
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


def get_langs_name(from_where):
    conn = db.connect()
    query_results = conn.execute('SELECT prof_Name FROM TrainedProf WHERE source_name = \''+from_where+'\' AND prof_Name in (SELECT Name from Proficiency WHERE Type = \'language\');').fetchall()
    conn.close()
    all = []
    for result in query_results:
        item = {
            "name"    : result[0],
        }
        all.append(item)

       

    if from_where  == 'Half-Elf':
        return all, 3
    elif from_where in ['Guild Artisan', 'Guild Merchant', 'Hermit', 'Noble', 'Knight', 'Outlander']:
        return all, 1
    elif from_where in ['Charlatan', 'Criminal', 'Spy', 'Entertainer', 'Gladiator','Folk Hero','Sailor','Pirate', 'Soldier','Urchin']:
        return all, 0

    

    return all, 2 


def get_equip_options(DNDclass):
    conn = db.connect()
    num_choice_list = conn.execute('SELECT DISTINCT choiceNumber FROM ClassEquipment WHERE className = \''+DNDclass+'\' ;').fetchall() 
    options = []
    for choice in num_choice_list:
        num_choice = str(choice[0])
        part = conn.execute('SELECT weaponName1, weaponName2, armorName1, armorName2, itemName1, itemName2 FROM ClassEquipment WHERE className = \''+DNDclass+'\' AND choiceNumber = '+num_choice+';').fetchall()
        new_part=[]
        for piece in part:
            little_part = []
            for equip in piece: 
                if equip != None:
                    little_part.append(equip)
                    if little_part not in new_part:
                        new_part.append(little_part)    

        options.append(new_part)
    conn.close()
    return options

def get_spell_options(DNDclass, level, user_name):
    if level == 0:
        level_name ='0'
    elif level == 1:
        level_name ='1'
    num_to_learn = 0
    conn = db.connect()
    num_choice_list = conn.execute('SELECT * FROM Spells WHERE classes = \''+DNDclass+'\'  AND level = \''+level_name+'\';').fetchall() 
    if level == 0:

        num_to_learn = conn.execute('SELECT cantrips FROM Magic WHERE className = \''+DNDclass+'\' AND level = 1 ').fetchall()
    elif level == 1:
        if DNDclass == "Fighter":
            num_to_learn = [[0]]
        elif DNDclass in ['Bard']:
            num_to_learn = [[4]]
        elif DNDclass in ['Cleric','Druid']:
            num_to_learn = conn.execute('SELECT WISmod FROM User_Character WHERE \''+user_name+'\' = PlayerName').fetchall()
        elif DNDclass in ['Wizard']:
            num_to_learn = conn.execute('SELECT INTmod FROM User_Character WHERE \''+user_name+'\' = PlayerName').fetchall()
    conn.close()

    num_to_learn = num_to_learn[0][0]

    if level == 1:
        num_to_learn +=1

    if num_to_learn == 0:
        num_to_learn = 1
    if num_to_learn == None:
        num_to_learn = 0
    return num_choice_list, num_to_learn


def get_background_info(background, info):
    conn = db.connect()

    information = conn.execute('SELECT * FROM BackgroundInfo WHERE backgroundName = \''+background+'\'  AND type = \''+info+'\';').fetchall() 
    clean_info =[]
    for part in information:
        clean_info.append(part[3])

    conn.close()
    return clean_info



def create_character(user_name):
     conn = db.connect()

     conn.execute('INSERT INTO User_Character(PlayerName) VALUES(\''+user_name+'\')')
     conn.close()

def update_character_value(field, value, user_name):
    conn = db.connect()

    conn.execute('UPDATE User_Character SET '+field+' = \''+value+'\' WHERE \''+user_name+'\' = PlayerName')
    conn.close()

def update_character_skills(values, user_name):
    conn = db.connect()
    dirty_skills = db.execute('SELECT Name from Proficiency WHERE Type = \'skill\';').fetchall()
    skills =[]
    for section in dirty_skills:
        skills.append(section[0])
    skills_boxes = ['Check_Box_23','Check_Box_24','Check_Box_25','Check_Box_26','Check_Box_27','Check_Box_28','Check_Box_29',\
        'Check_Box_30','Check_Box_31','Check_Box_32','Check_Box_33','Check_Box_34','Check_Box_35','Check_Box_36','Check_Box_37',\
            'Check_Box_38','Check_Box_39','Check_Box_40']

    for box in skills_boxes:
        conn.execute('UPDATE User_Character SET '+box+' = 0 WHERE \''+user_name+'\' = PlayerName')

   
    for skill in values:
        if skill in skills:
            index = skills.index(skill)
            conn.execute('UPDATE User_Character SET '+skills_boxes[index]+' = 1 WHERE \''+user_name+'\' = PlayerName')
    conn.close()


def update_character_langs(values, user_name):
    conn = db.connect()
    
    str_langs = ''
    for value in values:
        str_langs += value +', '
    str_langs = 'You know how to speak ' + str_langs[:len(str_langs)-2]

    conn.execute('UPDATE User_Character SET ProficienciesLang = \''+str_langs+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.close()

def update_character_equipment(values, user_name):
    words =''
    for part in values:
        word = ''
        for piece in part:
            if piece not in ["'",'"','/', '[', ']']:
                word += piece
        words += word + ', '
    words = words[:len(words)-2]

   
    conn = db.connect()
    conn.execute('UPDATE User_Character SET Equipment = \''+words+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.close()


def update_character_spells(values, user_name, spell_level):
    if spell_level == 0:
        boxes = ['Spells_1014', 'Spells_1016', 'Spells_1017', 'Spells_1018']
    elif spell_level == 1:
        boxes = ['Spells_1015', 'Spells_1023','Spells_1024', 'Spells_1025', 'Spells_1026', 'Spells_1027']
    conn = db.connect()
    
    for box in boxes:
        conn.execute('UPDATE User_Character SET '+box+' = \'None\' WHERE \''+user_name+'\' = PlayerName;')
    
    count = 0
    for spell in values:
        if spell != None:
            conn.execute('UPDATE User_Character SET '+boxes[count]+' = \''+spell+'\' WHERE \''+user_name+'\' = PlayerName;')
            count += 1
    
    
    conn.close()

def update_character_physical(values, user_name):
    conn = db.connect()
    

    conn.execute('UPDATE User_Character SET CharacterName = \''+values[0]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Alignment  = \''+values[1]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Age  = \''+values[2]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Eyes = \''+values[3]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Height  = \''+str(values[4])+' feet '+str(values[5])+' inches\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Weightt  = \''+values[6]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Skin  = \''+values[7]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Hair  = \''+values[8]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.close()

def update_character_bInfo(values, user_name):
    conn = db.connect()
    

    conn.execute('UPDATE User_Character SET PersonalityTraits = \''+values[0]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Ideals  = \''+values[1]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Bonds  = \''+values[2]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Flaws = \''+values[3]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.close()