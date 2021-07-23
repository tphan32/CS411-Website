from app import db
def get_weaponName():
    conn = db.connect()
    results = conn.execute('SELECT weaponName FROM Weapon;').fetchall()
    query_results = [x for x in results]
    conn.close()
    weaponName = []
    for result in query_results:
        weaponName.append(result[0])
    return weaponName

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