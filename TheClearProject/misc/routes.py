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

    return render_template('index.html')#, stations_lofd = stations, stations_json = json.dumps(stations))

@mod.route("/station_info")
def quote():
    station_id = request.args.get("station_id")
    station_id = 0
    # url = f"https://www.alphavantage.co/query?apikey=NAJXWIA8D6VN6A3K&datatype=csv&function=TIME_SERIES_INTRADAY&interval=1min&symbol={symbol}"
    # webpage = urllib.request.urlopen(url)
    # datareader = csv.reader(webpage.read().decode("utf-8").splitlines())
    # next(datareader)
    # row = next(datareader)
    station = json.dumps(config.db.execute("SELECT * FROM stations WHERE station_id = :station_id", station_id = station_id)[0])

    #For all stations
    station = json.dumps(config.db.execute("SELECT * FROM stations"))
    #print(station)
    return station
