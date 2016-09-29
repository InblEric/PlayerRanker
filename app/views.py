import pymongo
import configparser

from app import app
from pymongo import MongoClient
from flask import (render_template, request, redirect, url_for, session)

from utils import random_ops as rando

config = configparser.ConfigParser()
config.read("../config/config.cfg")

client = MongoClient()

week = "Week1"
# TODO:
# week = get_current_nfl_weel()
# formatted "Week1", "Week2", etc
db = client[week]
qbs = db.qb
rbs = db.rb
wrs = db.wr
tes = db.te


@app.route("/")
def hello():
    return render_template('home.html', week=week)

@app.route("/name")
def name():
    name = config.get("DEFAULT", "name")
    return "<h1 style='color:blue'>Hello, {0}!</h1>".format(name)

@app.route("/vote")
def vote():
    players = qbs.find()
    rands = rando.randomNums(players.count())
    comps = []
    comps.append(players[rands[0]])
    comps.append(players[rands[1]])
    return render_template('voting.html', players=comps, week=week)

@app.route("/rankings")
def rankings():
    return render_template('rankings.html')

@app.route("/quarterbacks")
def quarterbacks():
    players = qbs.find()
    return render_template('quarterbacks.html', players=players, week=week)

@app.route("/runningbacks")
def runningbacks():
    players = rbs.find()
    return render_template('runningbacks.html', players=players, week=week)

@app.route("/widereceivers")
def widereceivers():
    players = wrs.find()
    return render_template('widereceivers.html', players=players, week=week)

@app.route("/tightends")
def tightends():
    players = tes.find()
    return render_template('tightends.html', players=players, week=week)
