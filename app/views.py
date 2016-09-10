from app import app

from flask import (render_template, request, redirect, url_for, session)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello Eric!</h1>"

@app.route("/test")
def test():
    return "<h1 style='color:blue'>TEST!</h1>"
