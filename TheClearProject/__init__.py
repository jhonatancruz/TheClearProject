from flask import Flask
from cs50 import SQL

app = Flask(__name__)

#bot, login, misc, register are our individual blueprint folders.

from TheClearProject.bot.routes import mod
from TheClearProject.register.routes import mod
from TheClearProject.login.routes import mod
from TheClearProject.misc.routes import mod


#Url prefix will make prefix required. Omit to go straight from root. url_prefix = "/api"
app.register_blueprint(bot.routes.mod)
app.register_blueprint(register.routes.mod)
app.register_blueprint(login.routes.mod)
app.register_blueprint(misc.routes.mod)
