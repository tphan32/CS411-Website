from datetime import datetime
from app import database as db_helper
from app import app
from flask import render_template

@app.route("/")
def home():
    weaponName = db_helper.get_weaponName()
    return render_template("index.html", weaponName = weaponName)

@app.route("/query2")
def query2():
    items = db_helper.get_query_2()
    return render_template("query2.html", items = items)