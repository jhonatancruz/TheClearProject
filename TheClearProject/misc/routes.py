#!/usr/bin/python

from flask import Flask, render_template, request, Blueprint

mod = Blueprint('misc', __name__)

#Must use mod since we're in Blueprint

@mod.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@mod.route('/')
def index():
    return render_template('index.html')
