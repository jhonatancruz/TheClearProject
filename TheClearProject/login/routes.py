#!/usr/bin/python

from flask import Flask, render_template, request, Blueprint, flash, redirect, url_for
from cs50 import SQL
from .. import config

#REMOVE LIBRARIES IF NOT NEEDED
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

mod = Blueprint('login', __name__)

#Must use mod since we're in Blueprint

@mod.route('/userPage', methods=["GET","POST"])
def userPage():
    # where=config.db.execute("SELECT sponsor FROM stations WHERE station_id==(SELECT ))
    data= config.db.execute("SELECT pledge_description, pledge_date FROM helper_session WHERE helper_id==1")
    #when= config.db.execute("SELECT pledge_date FROM helper_session WHERE helper_id==1")
    # for x in what:
    #     print(x.values())
    # print(what[0]['pledge_description'])
    # print(what[1]['pledge_description'])
    return render_template("userPage.html", data=data)

@mod.route('/helper_session', methods=["GET", "POST"])
def helper_session():
    if request.method == "POST":
        station=request.form.get("stationid")
        pledge=request.form.get("pledge_descript")
        date=request.form.get("date")

        config.db.execute("INSERT INTO helper_session (helper_id, station_id, pledge_description, pledge_date) VALUES(1, :station, :pledge, :date_)",station=str(station), pledge=str(pledge), date_=str(date))
        # print(station, pledge, date)
        return redirect('/userPage')

        # config.db.execute("SELECT pledge_description, pledge_date FROM helper_session WHERE helper_id==1")

    return render_template('helper_session.html')


@mod.route('/login', methods=["GET", "POST"])
def login():
    """Log user in"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return("must provide password")

        # Query database for username
        # for numOfrows in len(config.db.execute("SELECT COUNT(*) FROM helper_users")
        user = config.db.execute("SELECT username, hash FROM helper_users")
        username= user[0]["username"]
        password= user[0]["hash"]

        print(username, password)


        if request.form.get("username")== username and request.form.get("password")== password:
            return redirect(url_for('login.userPage'))
        else:
            return render_template("login.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")
