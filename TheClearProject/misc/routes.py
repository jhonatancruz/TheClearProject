#!/usr/bin/python

from flask import Flask, render_template, request, Blueprint
from .. import config
import json

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
    stations = config.db.execute("SELECT * FROM stations")
    return render_template('index.html', stations_lofd = stations, stations_json = json.dumps(stations))
