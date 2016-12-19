import pymongo
import configparser

from app import app
from pymongo import MongoClient
from utils.weeks import get_current_nfl_week
from utils.sorting import sort_players
from flask import (render_template, request, redirect, url_for, session)

from utils import random_ops as rando

config = configparser.ConfigParser()
config.read("../config/config.cfg")

client = MongoClient()

week = get_current_nfl_week()
db = client[week]
qbs = db.qb
rbs = db.rb
wrs = db.wr
tes = db.te

@app.route("/")
def hello():
    #return render_template('home.html', week=week)
    return "Hello, World"

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

@app.route("/quarterbacks_std")
def quarterbacks_std():
    players = qbs.find()
    players = sort_players(players, key = "elo_std")
    return render_template('quarterbacks.html', players=players, week=week)

@app.route("/quarterbacks_6")
def quarterbacks_6():
    players = qbs.find()
    players = sort_players(players, key = "elo_6")
    return render_template('quarterbacks.html', players=players, week=week)

@app.route("/runningbacks_std")
def runningbacks_std():
    players = rbs.find()
    players = sort_players(players, key = "elo_std")
    return render_template('runningbacks.html', players=players, week=week)

@app.route("/runningbacks_half")
def runningbacks_half():
    players = rbs.find()
    players = sort_players(players, key = "elo_half")
    return render_template('runningbacks.html', players=players, week=week)

@app.route("/runningbacks_ppr")
def runningbacks_ppr():
    players = rbs.find()
    players = sort_players(players, key = "elo_ppr")
    return render_template('runningbacks.html', players=players, week=week)

@app.route("/widereceivers_std")
def widereceivers_std():
    players = wrs.find()
    players = sort_players(players, key = "elo_std")
    return render_template('widereceivers.html', players=players, week=week)

@app.route("/widereceivers_half")
def widereceivers_half():
    players = wrs.find()
    players = sort_players(players, key = "elo_half")
    return render_template('widereceivers.html', players=players, week=week)

@app.route("/widereceivers_ppr")
def widereceivers_ppr():
    players = wrs.find()
    players = sort_players(players, key = "elo_ppr")
    return render_template('widereceivers.html', players=players, week=week)

@app.route("/tightends_std")
def tightends_std():
    players = tes.find()
    players = sort_players(players, key = "elo_std")
    return render_template('tightends.html', players=players, week=week)

@app.route("/tightends_half")
def tightends_half():
    players = tes.find()
    players = sort_players(players, key = "elo_half")
    return render_template('tightends.html', players=players, week=week)

@app.route("/tightends_ppr")
def tightends_ppr():
    players = tes.find()
    players = sort_players(players, key = "elo_ppr")
    return render_template('tightends.html', players=players, week=week)
