import pymongo
import configparser

from app import app
from pymongo import MongoClient
from flask import (render_template, request, redirect, url_for, session)

config = configparser.ConfigParser()
config.read("../config/config.cfg")

client = MongoClient()

week = "Week1"
# TODO:
# week = get_current_nfl_weel()
# formatted "Week1", "Week2", etc
db = client[week]
qbs = db.qb


@app.route("/")
def hello():
    return render_template('home.html', week=week)

@app.route("/name")
def name():
    name = config.get("DEFAULT", "name")
    return "<h1 style='color:blue'>Hello, {0}!</h1>".format(name)

@app.route("/vote")
def vote():
    return render_template('voting.html')

@app.route("/rankings")
def rankings():
    return render_template('rankings.html')

@app.route("/quarterbacks")
def quarterbacks():
    players = qbs.find()
    return render_template('quarterbacks.html', players=players, week=week)
