# from twilio import twiml
# from math import cos, asin, sqrt
# from cs50 import SQL
# from twilio.twiml.messaging_response import MessagingResponse

from flask import Flask, flash, redirect, render_template, request, session


app= Flask(__name__)

# Databse Usage
db = SQL("sqlite:///database.db")
# use db.execute("YOUR SQL CODE HERE")
#   -- Will always return a list of dicts, which you must index into as follows
#   ----[int][key] like [0]["description"] will return first row's description
#
# phase = 0
# score = 0
# global locationSet
# locationSet = False
# key = 0

# # Ensure responses aren't cached
# @app.after_request
# def after_request(response):
#     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     response.headers["Expires"] = 0
#     response.headers["Pragma"] = "no-cache"
#     return response
#
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/register', methods=["GET", "POST"])
# def register():
#     """Register user"""
#     if request.method == "POST":
#
#         # Ensure username was submitted
#         if not request.form.get("username"):
#             return("must provide username")
#
#         # Ensure password AND confirmation was submitted
#         elif not request.form.get("password") or not request.form.get("confirmation"):
#             return("must provide and confirm password!")
#
#         # Ensure password matches confirmation.
#         elif request.form.get("password") != request.form.get("confirmation"):
#             return("passwords do not match!")
#
#         # Add username to  database, ensuring no 2 same usernames registered.
#         result = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=request.form.get(
#             "username"), hash=generate_password_hash(request.form.get("password")))
#         if not result:
#             return("username already exists!")
#
#         # Redirect user to home page
#         return redirect("/")
#
#     # User reached route via GET (as by clicking a link or via redirect)
#     else:
#         return render_template("register.html")

# @app.route('/login', methods=["GET", "POST"])
# def login():
#     """Log user in"""
#
#     # User reached route via POST (as by submitting a form via POST)
#     if request.method == "POST":
#
#         # Ensure username was submitted
#         if not request.form.get("username"):
#             return("must provide username")
#
#         # Ensure password was submitted
#         elif not request.form.get("password"):
#             return("must provide password")
#
#         # Query database for username
#         rows = db.execute("SELECT * FROM users WHERE username = :username",
#                           username=request.form.get("username"))
#
#         # Ensure username exists and password is correct
#         if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
#             return("invalid username and/or password")
#
#         # Redirect user to home page
#         return redirect("/")
#
#     # User reached route via GET (as by clicking a link or via redirect)
#     else:
#         return render_template("login.html")

#USELESS TEST?? HASN"T BEEN PORTED TO NEWEST.
# @app.route('/test')
# def test():
#     stations =  db.execute("SELECT * FROM stations")
#     for station in stations:
#         print(station["description"])
#     return render_template('maps.html')

# #bot for sat phones
# @app.route("/sms", methods=['GET', 'POST'])
# def sms_reply():
#     global phase
#     global longitude
#     global latitude
#     global score
#     global key
#
#     number = request.form['From']
#     message_body = request.form['Body']
#     message_body = message_body.strip()
#     message_body = message_body.lower()
#
#     print(message_body + "  "+ number)
#     resp = MessagingResponse()
#     #resp = twiml.Response()
#
#     print("PHASE: " + str(phase))
#     if phase == 0 :
#         phase = phase + 1
#         resp.message("Welcome! Please enter your Longitude and Latitude, seperated by a space")
#         return str(resp)
#
#     if phase == 1 :
#         coords = get_coords(message_body)
#
#         if is_valid_coords(coords) :
#             longitude = float(coords[0])
#             latitude = float(coords[1])
#
#             phase = 2
#             resp.message("Your location has been received! What would you like to do?((i)ssue, (o)ptions, (s)tatus, (f)inish)")
#
#             get_water_info(longitude, latitude)
#             return str(resp)
#         else :
#             resp.message("Invalid coordinates. Please enter your location in the format 12.345, 67.890")
#             return str(resp)
#
#     if phase == 2 :
#         if message_body.startswith("o") :
#             resp.message("Commands: (i)ssue, (o)ptions, (s)tatus, (f)inish")
#             return str(resp)
#
#         if message_body.startswith("i") :
#             phase = 3
#             resp.message("Alright, I've got a some questions for you...First, does the water system work at all? (y)es / (n)o")
#             return str(resp)
#
#         if message_body.startswith("f") :
#             phase = 0
#             resp.message("Thanks for stopping by. We're gonna get your issue taken care of and keep you posted with updates. Feel free to reach out to this bot at any time!")
#             return str(resp)
#
#         if message_body.startswith("s") :
#             resp.message(get_status() + " Would you like to do anything else? For a list of commands, type '(o)ptions'.")
#             return str(resp)
#
#         resp.message("Invalid Choice. For a list of commands, type 'options'")
#         return str(resp)
#
#     if phase == 3 :
#         if message_body.startswith("y") :
#             phase = 4
#             set_score(0)
#             resp.message("Alright that's good. Next, does the purification system provide ANY amount of clean water? (y)es / (n)o")
#             return str(resp)
#         if message_body.startswith("n") :
#             set_score(3)
#             resp.message("We've set your filtration repair to the HIGHEST PRIORITY. Please be patient, help is on the way.")
#             phase = 2
#             return str(resp)
#
#         resp.message("Invalid Input; Please answer with a (y)es or a (n)o.")
#         return str(resp)
#
#     if phase == 4 :
#         if message_body.startswith("y") :
#             phase = 5
#             set_score(0)
#             resp.message("Good. Give us a percentage (1 - 100) of the people in your community with access to clean water.")
#             return str(resp)
#         if message_body.startswith("n") :
#             set_score(3)
#             resp.message("We've set your filtration repair to the HIGHEST PRIORITY. Please be patient, help is on the way.")
#             phase = 2
#             return str(resp)
#
#         resp.message("Invalid Input; Please answer with a (y)es or a (n)o.")
#         return str(resp)
#
#     if phase == 5 :
#         if not is_valid_percent(message_body) :
#             resp.message("Invalid Input. Please answer with an estimate between 0 and 100.")
#             return str(resp)
#
#         percent = float(message_body)
#         phase = 6
#
#         if percent > 80 :
#             set_score(1)
#         elif percent > 65 :
#             set_score(2)
#         else :
#             set_score(3)
#
#         resp.message("Thank you, we've signalled for help. Would you like to leave any specific comments about your issue?")
#         return str(resp)
#
#     if phase == 6 :
#         if message_body.startswith("y") :
#             phase = 7
#             resp.message("Alright. Tell us details about your issue so we can better help you.")
#             return str(resp)
#         if message_body.startswith("n") :
#             resp.message("Okay. What else would you like to do? For a list of options, type (o)ptions. If there's nothing else, type (f)inish.")
#             phase = 2
#             return str(resp)
#
#         resp.message("Invalid Input; Please answer with a (y)es or a (n)o.")
#         return str(resp)
#
#     if phase == 7 :
#         log_issue_details(message_body)
#         phase = 2
#         resp.message("Your details have been logged. What else would you like to do? For a list of options, type (o)ptions. If there's nothing else, type (f)inish.")
#         return str(resp)
#
#     # print("NUMBER: " + number)
#     # print(message_body)
#
#     resp = MessagingResponse()
#
#     resp.message("The rabbits are coming")
#
#     return str(resp)
#
# #here we use the longitude and latitude provided to figure out which MySQL key we're gonna be accessing
# #when we update/pull from the database. score is used to assess damage done, perfect condition = 0, 3 = horrible,
# #4 = multiple people saying its horrible. 4 is the same as 3 on the map in terms of color and severity,
# #except we prioritize it above 3.
# def get_water_info(longitude, latitude) :
#
#     stations = db.execute("SELECT * FROM stations")
#
#     distance = 9999999
#     index = 0
#
#     for x in range(len(stations)):
#         lon = stations[x]["longitude"]
#         lat = stations[x]["latitude"]
#         dis = distance_coords(longitude, latitude, lon, lat)
#
#         if dis < distance :
#             index = x
#             distance = dis
#
#     key = index
#
#     print("KEY INDEX = " + str(key))
#
#     score = stations[key]["status"]
#
#     print("SCORE = " + str(score))
#
#     return
#
#
# #formats our long/lat input so that its more user friendly.
# def get_coords(str) :
#     coords = str.split(", ")
#
#     if len(coords) != 2 :
#         coords = str.split(" ")
#
#     if len (coords) != 2 :
#         coords = str.split(",")
#
#     return coords
#
# def get_status():
#     return "Your village kinda sucks, yo."
#
# #we keep track of the score for each water system.
# def inc_score(amount):
#     score = score + amount
#
#     if score > 4 :
#         score = 4
#
#     return
#
# #set_score tracks the score, and if it's higher than the current score in the database, it updates the DB.
# def set_score(amount) :
#     score = amount
#
#     return
#
# #here we update the database with issues. the row in question will be accessed through the key variable
# #and str will be ammended to the details section of the DB.
# def log_issue_details(str) :
#     return
#
# #given 2 long/latitudes, get the distance between them.
# def distance_coords(lat1, lon1, lat2, lon2):
#     p = 0.017453292519943295     #Pi/180
#     a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
#     return 12742 * asin(sqrt(a)) #2*R*asin...
#
# #returns true if the coordinates are actual floats.
# def is_valid_coords(s):
#     if len(s) == 2 :
#         if is_number(s[0]) and is_number(s[1]) :
#             return True
#     return False
#
# #for checking if coords are legit
# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         return False
#
# #is the number between 0 and 100?
# def is_valid_percent(s):
#     if not is_number(s):
#         return False
#     if float(s) > 100 or float(s) < 0:
#         return False
#     return True

if __name__ == '__main__':
    app.run(debug=True)
