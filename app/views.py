import configparser

from app import app
from flask import (render_template, request, redirect, url_for, session)

config = configparser.ConfigParser()
config.read("../config/config.cfg")

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Welcome to the Player Ranker!</h1>"

@app.route("/name")
def name():
    name = config.get("DEFAULT", "name")
    return "<h1 style='color:blue'>Hello, {0}!</h1>".format(name)
