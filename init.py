from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from flask_login import LoginManager
import routers,forms,models
#from models import User,registration,vinyl,papers



app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///base.db"
app.config["SECRET_KEY"]="secret_key_i_love-attack-on-titan"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
db=SQLAlchemy(app)
bootstrap=Bootstrap(app)
login=LoginManager()
login.login_view="sing_in"
login.init_app(app)




if __name__ == "__main__":
    app.run(debug=-True)
