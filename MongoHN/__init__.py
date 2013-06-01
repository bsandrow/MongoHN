""" MongoHN - A HackerNews clone using MongoDB + Flask """

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('MongoHN.config')

db = MongoEngine(app)

lm = LoginManager()
lm.init_app(app)

app.secret_key = 'daeh0leekae0Too0ohchai2Aiv8eev1maephuphiephohceeZ6chaihei8agh9aemaleij4Leel2neic2Inie0roh3'

from . import views, models
