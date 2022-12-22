from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Command,Shell
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import os,config 

app=Flask(__name__)
db=SQLAlchemy(app)
bootstrap=Bootstrap(app)
login_manager=LoginManager(app)
login_manager.login_view='login'

from . import views

