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
    print(backgrounds)
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
        if DNDclass == "Fighter":
            num_to_learn = [[0]]
        elif DNDclass in ['Bard']:
            num_to_learn = [[4]]
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
    
    for part in values:
        thing = ''
        for piece in part:
            if piece == "'":
                thing += "''"
            else:
                thing += piece
        values[values.index(part)] = thing                
        
    conn.execute('UPDATE User_Character SET PersonalityTraits = \''+values[0]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Ideals  = \''+values[1]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Bonds  = \''+values[2]+'\' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET Flaws = \''+values[3]+'\' WHERE \''+user_name+'\' = PlayerName;')
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

    print(skills)
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
    HP = conn.execute('SELECT hitPoints FROM Class WHERE className = \''+DNDclass+'\';').fetchall()
    HP = HP[0][0]
    totalHP = HP + CONmod
    totalHP = str(totalHP)
    conn.execute('UPDATE User_Character SET HPMax = '+totalHP+' WHERE \''+user_name+'\' = PlayerName;')
    conn.execute('UPDATE User_Character SET HPCurrent = '+totalHP+' WHERE \''+user_name+'\' = PlayerName;')

