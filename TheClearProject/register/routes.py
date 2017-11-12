#!/usr/bin/python

from flask import Flask, render_template, request, Blueprint
from .. import config

#REMOVE LOGINS IF NOT NEEDED
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

mod = Blueprint('register', __name__)

#Must use mod since we're in Blueprint

@mod.route('/register', methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return("must provide username")

        # Ensure password AND confirmation was submitted
        elif not request.form.get("password") or not request.form.get("confirmation"):
            return("must provide and confirm password!")

        # Ensure password matches confirmation.
        elif request.form.get("password") != request.form.get("confirmation"):
            return("passwords do not match!")

        # Add username to  database, ensuring no 2 same usernames registered.
        result = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=request.form.get(
            "username"), hash=generate_password_hash(request.form.get("password")))
        if not result:
            return("username already exists!")

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")
