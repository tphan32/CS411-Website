from typing import List
from app import db
import pdfrw

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

def call_pro_rand_spell():
    conn = db.connect()
    query = "CALL randomNewSpell();"
    query_results = conn.execute(query).fetchall()
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

def insert_weapon(input: List[str]):
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

# def searchDB(key):
#     conn = db.connect()
#     # Use %% https://stackoverflow.com/questions/42153376/python-mysql-error-when-i-use-s-in-execute
#     q = 'SELECT * FROM Weapon WHERE weaponName LIKE "{}"'.format(key+"%%") + ";"
#     shows = conn.execute(q).fetchall()
#     conn.close()
#     items = []
#     for result in shows:
#         item = {
#             "weaponName": result[0],
#         } 
#         items.append(item)
#     return items

def lookupDesc(table, cond, key):
    conn = db.connect()
    query = "SELECT description FROM {} WHERE {} LIKE '{}';".format(table, cond, key+"%%")
    ret = conn.execute(query).fetchall()
    conn.close()
    return ret[0][0]

def get_spellInfo():
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

def get_raceInfo():
    conn = db.connect()
    query_results = conn.execute('SELECT * FROM Race ORDER BY speed;').fetchall()
    conn.close()
    items = []
    for result in query_results:
        item = {
            "name"    : result[0],
            "subrace"   : result[1],
            "abilityScoreIncrease1"  : result[2],
            "abilityScoreIncrease2": result[3],
            "ability1": result[4],
            "ability2": result[5],
            "ageRange": result[6],
            "description": result[7],
            "size": result[8],
            "speed": result[9]
        } 
        items.append(item)
    return items

def get_classInfo():
    conn = db.connect()
    query_results = conn.execute('SELECT * FROM Class ORDER BY hitPoints;').fetchall()
    conn.close()
    items = []
    for result in query_results:
        item = {
            "name"    : result[0],
            "subclass"   : result[1],
            "hitPoints"  : result[2],
            "description": result[3],
            "gold": result[4],
            "spellCastAbility": result[5],
        } 
        items.append(item)
    return items

def get_bckgInfo():
    conn = db.connect()
    query_results = conn.execute('SELECT * FROM Background;').fetchall()
    conn.close()
    items = []
    for result in query_results:
        item = {
            "name"    : result[0],
            "description": result[1],
            "equipment": result[2],
        } 
        items.append(item)
    return items

def get_armorInfo():
    conn = db.connect()
    query_results = conn.execute('SELECT * FROM Armor;').fetchall()
    conn.close()
    items = []
    for result in query_results:
        item = {
            "name"    : result[0],
            "cost"   : result[1],
            "armorClass"  : result[2],
            "strNeeded": result[3],
            "stealthDisadv": result[4],
            "weight": result[5],
            "category": result[6]
        } 
        items.append(item)
    return items

def get_armorInfo():
    conn = db.connect()
    query_results = conn.execute('SELECT * FROM Armor;').fetchall()
    conn.close()
    items = []
    for result in query_results:
        item = {
            "name"    : result[0],
            "cost"   : result[1],
            "armorClass"  : result[2],
            "strNeeded": result[3],
            "stealthDisadv": result[4],
            "weight": result[5],
            "category": result[6]
        } 
        items.append(item)
    return items

def get_genItemInfo():
    conn = db.connect()
    query_results = conn.execute('SELECT * FROM GeneralItem;').fetchall()
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

def get_profInfo():
    conn = db.connect()
    query_results = conn.execute('SELECT * FROM Proficiency;').fetchall()
    conn.close()
    items = []
    for result in query_results:
        item = {
            "name"    : result[0],
            "type"   : result[1],
            "subtype"  : result[2],
            "description": result[3]
        } 
        items.append(item)
    return items

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
    query_results = conn.execute('SELECT prof_Name FROM TrainedProf WHERE source_name = \''+from_where+'\' AND prof_Name in (SELECT profName from Proficiency WHERE Type = \'skill\');').fetchall()
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
    query_results = conn.execute('SELECT prof_Name FROM TrainedProf WHERE source_name = \''+from_where+'\' AND prof_Name in (SELECT profName from Proficiency WHERE Type = \'language\');').fetchall()
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
        if DNDclass == "Fighter" or DNDclass == "Paladin":
            num_to_learn = [[0]]
        elif DNDclass in ['Bard']:
            num_to_learn = [[4]]
            ABBB = conn.execute('SELECT Chamod FROM User_Character WHERE \''+user_name+'\' = PlayerName').fetchall()
            save = str(ABBB[0][0] + 10)
            atk = str(ABBB[0][0] + 12)
            conn.execute('UPDATE User_Character SET SpellcastingAbility_2 = \'CHA\' WHERE \''+user_name+'\' = PlayerName;')
            conn.execute('UPDATE User_Character SET SpellSaveDC_2 = '+save+' WHERE \''+user_name+'\' = PlayerName;')
            conn.execute('UPDATE User_Character SET SpellAtkBonus_2 = '+atk+' WHERE \''+user_name+'\' = PlayerName;')
            conn.execute('UPDATE User_Character SET Spellcasting_Class_2 = \''+DNDclass+'\' WHERE \''+user_name+'\' = PlayerName;')
        elif DNDclass in ['Cleric','Druid']:
            num_to_learn = conn.execute('SELECT WISmod FROM User_Character WHERE \''+user_name+'\' = PlayerName').fetchall()
            save = str(num_to_learn[0][0] + 10)
            atk = str(num_to_learn[0][0] + 12)
            conn.execute('UPDATE User_Character SET SpellcastingAbility_2 = \'WIS\' WHERE \''+user_name+'\' = PlayerName;')
            conn.execute('UPDATE User_Character SET SpellSaveDC_2 = '+save+' WHERE \''+user_name+'\' = PlayerName;')
            conn.execute('UPDATE User_Character SET SpellAtkBonus_2 = '+atk+' WHERE \''+user_name+'\' = PlayerName;')
            conn.execute('UPDATE User_Character SET Spellcasting_Class_2 = \''+DNDclass+'\' WHERE \''+user_name+'\' = PlayerName;')
        elif DNDclass in ['Wizard']:
            num_to_learn = conn.execute('SELECT INTmod FROM User_Character WHERE \''+user_name+'\' = PlayerName').fetchall()
            save = str(num_to_learn[0][0] + 10)
            atk = str(num_to_learn[0][0] + 12)
            conn.execute('UPDATE User_Character SET SpellcastingAbility_2 = \'INT\' WHERE \''+user_name+'\' = PlayerName;')
            conn.execute('UPDATE User_Character SET SpellSaveDC_2 = '+save+' WHERE \''+user_name+'\' = PlayerName;')
            conn.execute('UPDATE User_Character SET SpellAtkBonus_2 = '+atk+' WHERE \''+user_name+'\' = PlayerName;')
            conn.execute('UPDATE User_Character SET Spellcasting_Class_2 = \''+DNDclass+'\' WHERE \''+user_name+'\' = PlayerName;')
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
    dirty_skills = db.execute('SELECT profName from Proficiency WHERE Type = \'skill\';').fetchall()
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
    conn = db.connect()
    dirty_armor = conn.execute('SELECT armorName FROM Armor ;').fetchall()
    armor = []
    for part in dirty_armor:
        armor.append(part[0])
    
    dirty_AC = conn.execute('SELECT armorClass FROM Armor ;').fetchall()
    AC = []
    for part in dirty_AC:
        AC.append(part[0])

    dex_add = [0,2,3,4,5,6,9,12]
    dex_limit = [0,2,3,4,9]
    
    

    DEXmod = conn.execute('SELECT DEXmod FROM User_Character WHERE \''+user_name+'\' = PlayerName;').fetchall()[0][0]
   
    Char_AC = 10 + DEXmod

    words =''
    for part in values:
        word = ''
        for piece in part:
            if piece not in ["'",'"','/', '[', ']', ',']:
                word += piece
        words += word + ', '
        for arm in armor:
            if arm in word and arm != 'Shield':
                index = armor.index(arm)
                Char_AC = int(AC[index][:2])
                if index in dex_add and index not in dex_limit:

                    Char_AC += DEXmod

                elif index in dex_add and index in dex_limit:
                    if DEXmod > 2:
                        Char_AC += 2
                    else:
                        Char_AC += DEXmod
            if 'Shield' in word:
                Char_AC += 2


    Char_AC = str(Char_AC)
    conn.execute('UPDATE User_Character SET AC = '+Char_AC+' WHERE \''+user_name+'\' = PlayerName;')
    
    
    
    words = words[:len(words)-2]
    
    BG = conn.execute('SELECT Background FROM User_Character WHERE \''+user_name+'\' = PlayerName;').fetchall()[0][0]
    BGEquip = conn.execute('SELECT equipment FROM Background WHERE bgName = \''+BG+'\';').fetchall()[0][0]
    
    words += "\n\n" + BGEquip 
    conn.execute('UPDATE User_Character SET Equipment = \''+words+'\' WHERE \''+user_name+'\' = PlayerName;')
    
    
    
    dirty_weapons = conn.execute('SELECT WeaponName, damage, damageType FROM Weapon ;').fetchall()
    WpnName = []
    WpnDmg = []
    WpnDmgType = []
    for weaponInfo in dirty_weapons:
        if weaponInfo[0] in words:
            WpnName.append(weaponInfo[0])
            WpnDmg.append(weaponInfo[1])
            WpnDmgType.append(weaponInfo[2])
    print(WpnName)
    print(WpnDmg)
    print(WpnDmgType)
    
    if len(WpnName) > 0:
        conn.execute('UPDATE User_Character SET Wpn_Name = \''+WpnName[0]+'\' WHERE \''+user_name+'\' = PlayerName;')
        conn.execute('UPDATE User_Character SET Wpn1_AtkBonus = \''+WpnDmg[0]+'\' WHERE \''+user_name+'\' = PlayerName;')
        conn.execute('UPDATE User_Character SET Wpn1_Damage = \''+WpnDmgType[0]+'\' WHERE \''+user_name+'\' = PlayerName;')
    if len(WpnName) > 1:
        conn.execute('UPDATE User_Character SET Wpn_Name2 = \''+WpnName[1]+'\' WHERE \''+user_name+'\' = PlayerName;')
        conn.execute('UPDATE User_Character SET Wpn2_AtkBonus = \''+WpnDmg[1]+'\' WHERE \''+user_name+'\' = PlayerName;')
        conn.execute('UPDATE User_Character SET Wpn2_Damage = \''+WpnDmgType[1]+'\' WHERE \''+user_name+'\' = PlayerName;')
    if len(WpnName) > 2:
        conn.execute('UPDATE User_Character SET Wpn_Name3 = \''+WpnName[2]+'\' WHERE \''+user_name+'\' = PlayerName;')
        conn.execute('UPDATE User_Character SET Wpn3_AtkBonus = \''+WpnDmg[2]+'\' WHERE \''+user_name+'\' = PlayerName;')
        conn.execute('UPDATE User_Character SET Wpn3_Damage = \''+WpnDmgType[2]+'\' WHERE \''+user_name+'\' = PlayerName;')



    


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
    
    for part in values:
        thing = ''
        for piece in part:
            if piece == "'":
                thing += "''"
            else:
                thing += piece
        values[values.index(part)] = thing                

    back = conn.execute('SELECT Background FROM User_Character WHERE \''+user_name+'\' = PlayerName;').fetchall()[0][0]
    backstory = conn.execute('SELECT description FROM Background WHERE bgName = \''+back+'\';').fetchall()[0][0]

    new_backstory = ''
    for piece in backstory:
        if piece == "'":
            new_backstory += "''"
        else:
            new_backstory += piece 
    conn.execute('UPDATE User_Character SET PersonalityTraits = \''+values[0]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Ideals  = \''+values[1]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Bonds  = \''+values[2]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Flaws = \''+values[3]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Backstory = \''+new_backstory+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.close()

def update_character_ST(user_name):
    conn = db.connect()
    #SELECT CLASS
    DNDclass = conn.execute('SELECT ClassLevel FROM User_Character WHERE \''+user_name+'\' = PlayerName;').fetchall()
    DNDclass= DNDclass[0][0]
    DNDclass = DNDclass[:len(DNDclass)-1]

    ABMOD = conn.execute('SELECT STRmod, DEXmod, CONmod, INTmod, WISmod, CHamod FROM User_Character WHERE \''+user_name+'\' = PlayerName;').fetchall()
    ABMOD = ABMOD[0]
    #SAVING THROWS

    AB_list = ['Strength', 'Dexterity','Constitution','Intelligence','Wisdom','Charisma']
    ST_mod = ['ST_Strength', 'ST_Dexterity','ST_Constitution','ST_Intelligence','ST_Wisdom','ST_Charisma']

    ST_AB = conn.execute('SELECT prof_name FROM TrainedProf WHERE \''+DNDclass+'\' = source_name AND prof_name not in (SELECT ProfName from Proficiency);').fetchall()
    ST1 = ST_AB[0][0]
    ST2 = ST_AB[1][0]

    ST_Boxes = ['Check_Box_11','Check_Box_18','Check_Box_19','Check_Box_20','Check_Box_21','Check_Box_22']
    
    for AB in AB_list:
        if AB == ST1:
            index = AB_list.index(AB)
            value = ABMOD[index] + 2
            value = str(value)
            conn.execute('UPDATE User_Character SET '+ ST_mod[index] +' = \''+value+'\' WHERE \''+user_name+'\' = PlayerName;')
            conn.execute('UPDATE User_Character SET '+ ST_Boxes[index] +' = 1 WHERE \''+user_name+'\' = PlayerName;')
        if AB == ST2:
            index = AB_list.index(AB)
            value = ABMOD[index] + 2
            value = str(value)
            conn.execute('UPDATE User_Character SET '+ ST_mod[index] +' = \''+value+'\' WHERE \''+user_name+'\' = PlayerName;')
            conn.execute('UPDATE User_Character SET '+ ST_Boxes[index] +' = 1 WHERE \''+user_name+'\' = PlayerName;')
        else:
            index = AB_list.index(AB)
            value = ABMOD[index]
            value = str(value) 
            conn.execute('UPDATE User_Character SET '+ ST_mod[index] +' = \''+value+'\' WHERE \''+user_name+'\' = PlayerName;')

def update_character_prof_mod(user_name):
    conn = db.connect()
    AB = conn.execute('SELECT DISTINCT prof_name FROM TrainedProf WHERE prof_name not in (SELECT ProfName from Proficiency);').fetchall()
    new_AB = []
    for part in AB:
        piece = part[0]
        new_AB.append(piece)
    #reorder
    #new_AB is names
    new_AB[0],new_AB[1],new_AB[2],new_AB[3],new_AB[4],new_AB[5] = new_AB[4],new_AB[2],new_AB[1],new_AB[3],new_AB[5],new_AB[0]
    new_AB.remove('Constitution')
    
    #These are modifiers
    ABMOD = conn.execute('SELECT STRmod, DEXmod, CONmod, INTmod, WISmod, CHamod FROM User_Character WHERE \''+user_name+'\' = PlayerName;').fetchall()
    ABMOD = ABMOD[0]
    new_ABMOD = []
    for item in ABMOD:
        new_ABMOD.append(item)
    ABMOD = new_ABMOD
    del ABMOD[2]
  

    #skillNames
    dirty_skills = db.execute('SELECT ProfName from Proficiency WHERE Type = \'skill\';').fetchall()
    skills =[]
    for section in dirty_skills:
        skills.append(section[0])
    #skill check boxes
    skills_boxes = ['Check_Box_23','Check_Box_24','Check_Box_25','Check_Box_26','Check_Box_27','Check_Box_28','Check_Box_29',\
        'Check_Box_30','Check_Box_31','Check_Box_32','Check_Box_33','Check_Box_34','Check_Box_35','Check_Box_36','Check_Box_37',\
            'Check_Box_38','Check_Box_39','Check_Box_40']


    #AB link skill
    skillSTR = ['Athletics']
    skillDEX = ['Acrobatics','Sleight of Hand','Stealth']
    skillINT = ['Arcana','History','Investigation','Nature','Religion']
    skillWIS = ['Animal Handling','Insight','Medicine','Perception','Survival']
    skillCHA = ['Deception','Intimidation','Performance','Persuasion']

    skillAB = [skillSTR,skillDEX,skillINT,skillWIS,skillCHA]

    for skill in skills:
        for ABskill in skillAB:
            if skill in ABskill:
                index = skillAB.index(ABskill)
                index2 = skills.index(skill)
                is_prof = conn.execute('SELECT '+skills_boxes[index2] +' FROM User_Character WHERE \''+user_name+'\' = PlayerName;').fetchall()
                
                new_prof = int.from_bytes(is_prof[0][0], byteorder ='little' )
  
                value = ABMOD[index] + 2 * new_prof
                value = str(value)

                underSkill = skill
                newUnderSkill = ''
                for i in underSkill:
                    if i == ' ':
                        newUnderSkill += '_'
                    else:
                        newUnderSkill += i


                conn.execute('UPDATE User_Character SET '+ newUnderSkill +' = '+value+' WHERE \''+user_name+'\' = PlayerName;')
    passive = ABMOD[4]+10
    passive = str(passive)
    conn.execute('UPDATE User_Character SET Passive = '+passive+' WHERE \''+user_name+'\' = PlayerName;')

def update_character_MISC(user_name):
    conn = db.connect()
    initiative = conn.execute('SELECT DEXmod FROM User_Character WHERE \''+user_name+'\' = PlayerName;').fetchall()
    initiative = initiative[0][0]
    initiative = str(initiative)
    conn.execute('UPDATE User_Character SET Initiative = '+initiative+' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Speed = 30 WHERE \''+user_name+'\' = PlayerName;')

    CONmod = conn.execute('SELECT CONmod FROM User_Character WHERE \''+user_name+'\' = PlayerName;').fetchall()
    CONmod = CONmod[0][0]
    DNDclass = conn.execute('SELECT ClassLevel FROM User_Character WHERE \''+user_name+'\' = PlayerName;').fetchall()
    DNDclass= DNDclass[0][0]
    DNDclass = DNDclass[:len(DNDclass)-1]

    DNDrace = conn.execute('SELECT Race FROM User_Character WHERE \''+user_name+'\' = PlayerName;').fetchall()
    DNDrace= DNDrace[0][0]


    HP = conn.execute('SELECT hitPoints FROM Class WHERE className = \''+DNDclass+'\';').fetchall()
    HP = HP[0][0]
    totalHP = HP + CONmod
    totalHP = str(totalHP)
    conn.execute('UPDATE User_Character SET HPMax = '+totalHP+' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET HPCurrent = '+totalHP+' WHERE \''+user_name+'\' = PlayerName;')

    slot = conn.execute('SELECT slotsLvl1 FROM Magic WHERE \''+DNDclass+'\' = className;').fetchall()[0][0]
    if slot != None: 
        slot = str(slot)
    else:
        slot = 0
        slot = str(slot)
    conn.execute('UPDATE User_Character SET SlotsTotal_19 = '+slot+' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET SlotsRemaining_19 = '+slot+' WHERE \''+user_name+'\' = PlayerName;')
    
    ClassFeatures = conn.execute('SELECT featureName, description FROM ClassFeature WHERE \''+DNDclass+'\' = className AND classLevel = 1;').fetchall()
    RaceFeatures = conn.execute('SELECT featureName, description FROM RaceFeature WHERE \''+DNDrace+'\' = raceName;').fetchall()
    
    new_class_features = ''
    for feature in ClassFeatures:
        if feature[0] != 'Spellcasting':
            new_feature = ''
            for piece in feature[1]:
                if piece == "'":
                    new_feature += "''"
                else:
                    new_feature += piece 
            new_class_features += feature[0]+ ": " +new_feature + '     \n\n'

    new_race_features = ''
    for feature in RaceFeatures:
            new_feature = ''
            for piece in feature[1]:
                if piece == "'":
                    new_feature += "''"
                else:
                    new_feature += piece 
            new_race_features += feature[0]+ ": " +feature[1] + '     \n\n'

    print(len(new_class_features))
    print(len(new_race_features))


    conn.execute('UPDATE User_Character SET  FeatANDTraits = \''+new_class_features+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Features_and_Traits = \' '+new_race_features+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.close()


def get_char_info(user_name):
    conn = db.connect()
    char_info = conn.execute('SELECT * FROM User_Character WHERE \''+user_name+'\' = PlayerName;').fetchall()
    char_info_name = conn.execute('SHOW COLUMNS FROM User_Character;').fetchall()
    conn.close()
    return char_info, char_info_name

def fillPDF(username):
    pdf_template = "CHAR.pdf"
    pdf_output = "C:\\Users\\jtw19\\Documents\\github\\DndWebsite\\CS411-Website\\app\\templates\\Output.pdf"
    path = "C:\\Users\\jtw19\\Documents\\github\\DndWebsite\\CS411-Website\\app\\CHAR.pdf"

    template_pdf = pdfrw.PdfReader(path)

    ANNOT_KEY = '/Annots'
    ANNOT_FIELD_KEY = '/T'
    ANNOT_VAL_KEY = '/V'
    ANNOT_RECT_KEY = '/Rect'
    SUBTYPE_KEY = '/Subtype'
    WIDGET_SUBTYPE_KEY = '/Widget'

    #Test code to print out all the keys:
    # for page in template_pdf.pages:
    #     annotations = page[ANNOT_KEY]
    #     for annotation in annotations:
    #         if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
    #             if annotation[ANNOT_FIELD_KEY]:
    #                 key = annotation[ANNOT_FIELD_KEY][1:-1]
    #                 print(key)

    conn = db.connect()
    data_dict = {
        'PlayerName': conn.execute('SELECT PlayerName FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'CharacterName': conn.execute('SELECT CharacterName FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'CharacterName 2': conn.execute('SELECT CharacterName FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'ClassLevel': conn.execute('SELECT ClassLevel FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0], #+ ' Level 1'
        'Background': conn.execute('SELECT Background FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Race ': conn.execute('SELECT Race FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Alignment': conn.execute('SELECT Alignment FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],

        'STR': conn.execute('SELECT STR FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'DEX': conn.execute('SELECT DEX FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'CON': conn.execute('SELECT CON FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'INT': conn.execute('SELECT INTT FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'WIS': conn.execute('SELECT WIS FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'CHA': conn.execute('SELECT CHA FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'STRmod': conn.execute('SELECT STRmod FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'DEXmod ': conn.execute('SELECT DEXmod FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'CONmod': conn.execute('SELECT CONmod FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'INTmod': conn.execute('SELECT INTmod FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'WISmod': conn.execute('SELECT WISmod FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'CHamod': conn.execute('SELECT CHamod FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        
        'ProfBonus': conn.execute('SELECT ProfBonus FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],

        'Check Box 11': conn.execute('SELECT Check_Box_11 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 18': conn.execute('SELECT Check_Box_18 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 19': conn.execute('SELECT Check_Box_19 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 20': conn.execute('SELECT Check_Box_20 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 21': conn.execute('SELECT Check_Box_21 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 22': conn.execute('SELECT Check_Box_22 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],

        'ST Strength': conn.execute('SELECT ST_Strength FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'ST Dexterity': conn.execute('SELECT ST_Dexterity FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'ST Constitution': conn.execute('SELECT ST_Constitution FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'ST Intelligence': conn.execute('SELECT ST_Intelligence FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'ST Wisdom': conn.execute('SELECT ST_Wisdom FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'ST Charisma': conn.execute('SELECT ST_Charisma FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],

        'Check Box 23': conn.execute('SELECT Check_Box_23 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 24': conn.execute('SELECT Check_Box_24 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 25': conn.execute('SELECT Check_Box_25 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 26': conn.execute('SELECT Check_Box_26 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 27': conn.execute('SELECT Check_Box_27 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 28': conn.execute('SELECT Check_Box_28 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 29': conn.execute('SELECT Check_Box_29 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 30': conn.execute('SELECT Check_Box_30 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 31': conn.execute('SELECT Check_Box_31 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 32': conn.execute('SELECT Check_Box_32 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 33': conn.execute('SELECT Check_Box_33 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 34': conn.execute('SELECT Check_Box_34 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 35': conn.execute('SELECT Check_Box_35 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 36': conn.execute('SELECT Check_Box_36 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 37': conn.execute('SELECT Check_Box_37 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 38': conn.execute('SELECT Check_Box_38 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 39': conn.execute('SELECT Check_Box_39 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Check Box 40': conn.execute('SELECT Check_Box_40 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],

        'Acrobatics': conn.execute('SELECT Acrobatics FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Animal': conn.execute('SELECT Animal_Handling FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Arcana': conn.execute('SELECT Arcana FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Athletics': conn.execute('SELECT Athletics FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Deception ': conn.execute('SELECT Deception FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'History': conn.execute('SELECT History FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Insight': conn.execute('SELECT Insight FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Intimidation': conn.execute('SELECT Intimidation FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Investigation ': conn.execute('SELECT Investigation FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Medicine': conn.execute('SELECT Medicine FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Nature': conn.execute('SELECT Nature FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Perception ': conn.execute('SELECT Perception FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Performance': conn.execute('SELECT Performance FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Persuasion': conn.execute('SELECT Persuasion FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Religion': conn.execute('SELECT Religion FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'SleightofHand': conn.execute('SELECT Sleight_of_Hand FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Stealth ': conn.execute('SELECT Stealth FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Survival': conn.execute('SELECT Survival FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Passive': conn.execute('SELECT Passive FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'ProficienciesLang': conn.execute('SELECT ProficienciesLang FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],

        'AC': conn.execute('SELECT AC FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Initiative': conn.execute('SELECT Initiative FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Speed': conn.execute('SELECT Speed FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'HPMax': conn.execute('SELECT HPMax FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'HPCurrent': conn.execute('SELECT HPCurrent FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],

        'Wpn Name': conn.execute('SELECT Wpn_Name FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Wpn1 AtkBonus': conn.execute('SELECT Wpn1_AtkBonus FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Wpn1 Damage': conn.execute('SELECT Wpn1_Damage FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        
        'Wpn Name 2': conn.execute('SELECT Wpn_Name2 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Wpn2 AtkBonus ': conn.execute('SELECT Wpn2_AtkBonus FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Wpn2 Damage ': conn.execute('SELECT Wpn2_Damage FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],

        'Wpn Name 3': conn.execute('SELECT Wpn_Name3 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Wpn3 AtkBonus  ': conn.execute('SELECT Wpn3_AtkBonus FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Wpn3 Damage ': conn.execute('SELECT Wpn3_Damage FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],

        'AttacksSpellcasting': conn.execute('SELECT AttacksSpellcasting FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Equipment': conn.execute('SELECT Equipment FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],

        'PersonalityTraits ': conn.execute('SELECT PersonalityTraits FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Ideals': conn.execute('SELECT Ideals FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Bonds': conn.execute('SELECT Bonds FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Flaws': conn.execute('SELECT Flaws FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],

        'Features and Traits': conn.execute('SELECT Features_and_Traits FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],

        'Age': conn.execute('SELECT Age FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Height': conn.execute('SELECT Height FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Weight': conn.execute('SELECT Weightt FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Eyes': conn.execute('SELECT Eyes FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Skin': conn.execute('SELECT Skin FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Hair': conn.execute('SELECT Hair FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Backstory': conn.execute('SELECT Backstory FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Feat+Traits': conn.execute('SELECT FeatANDTraits FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],

        'Spellcasting Class 2': conn.execute('SELECT Spellcasting_Class_2 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'SpellcastingAbility 2': conn.execute('SELECT SpellcastingAbility_2 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'SpellSaveDC  2': conn.execute('SELECT SpellSaveDC_2 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'SpellAtkBonus 2': conn.execute('SELECT SpellAtkBonus_2 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],

        'Spells 1014': conn.execute('SELECT Spells_1014 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Spells 1016': conn.execute('SELECT Spells_1016 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Spells 1017': conn.execute('SELECT Spells_1017 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Spells 1018': conn.execute('SELECT Spells_1018 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],

        'SlotsTotal 19': conn.execute('SELECT SlotsTotal_19 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'SlotsRemaining 19': conn.execute('SELECT SlotsRemaining_19 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],

        'Spells 1015': conn.execute('SELECT Spells_1015 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Spells 1023': conn.execute('SELECT Spells_1023 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Spells 1024': conn.execute('SELECT Spells_1024 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Spells 1025': conn.execute('SELECT Spells_1025 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Spells 1026': conn.execute('SELECT Spells_1026 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0],
        'Spells 1027': conn.execute('SELECT Spells_1027 FROM User_Character WHERE \''+username+'\' = PlayerName;').fetchall()[0][0]
    }

    conn.close()

    #for part in data_dict:
        #print(part,data_dict[part], type(data_dict[part]))

    def fill_pdf(input_pdf_path, output_pdf_path, data_dict):
        template_pdf = pdfrw.PdfReader(input_pdf_path)
        template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
        for page in template_pdf.pages:
            annotations = page[ANNOT_KEY]
            for annotation in annotations:
                if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                    if annotation[ANNOT_FIELD_KEY]:
                        key = annotation[ANNOT_FIELD_KEY][1:-1]
                        #print('key',key + 'lol')
                        if key in data_dict.keys():
                            if type(data_dict[key]) == bytes:
                                if data_dict[key] == b'\x01':
                                    annotation.update(pdfrw.PdfDict(
                                        AS=pdfrw.PdfName('Yes')))
                            else:
                                annotation.update(
                                    pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                                )
                                annotation.update(pdfrw.PdfDict(AP=''))
        pdfrw.PdfWriter().write(output_pdf_path, template_pdf)

    fill_pdf(path, pdf_output, data_dict)

