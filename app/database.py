from typing import List
from app import db
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
