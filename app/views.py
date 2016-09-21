import pymongo
import configparser

from app import app
from pymongo import MongoClient
from flask import (render_template, request, redirect, url_for, session)

config = configparser.ConfigParser()
config.read("../config/config.cfg")

client = MongoClient()

db = client.test
entries_collection = db.entries

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/name")
def name():
    name = config.get("DEFAULT", "name")
    return "<h1 style='color:blue'>Hello, {0}!</h1>".format(name)

@app.route("/test")
def test():
    entries = entries_collection.find()[0].get("entries1")
    html = ""
    for entry in entries:
        html = html + "\n<h1 style='color:blue'>Entry: {0}!</h1>".format(int(entry))
    return html
