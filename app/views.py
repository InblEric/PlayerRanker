from app import app

from flask import (render_template, request, redirect, url_for, session)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Welcome to the Player Ranker!</h1>"
