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
    return render_template("userPage.html")

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

        if request.form.get("username")== username and request.form.get("password")== password:
            return redirect(url_for('login.userPage'))
        else:
            return render_template("login.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")
