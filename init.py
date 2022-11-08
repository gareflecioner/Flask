from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///base.db"
app.config["SECRET_KEY"]="secret_key_i_love-attack-on-titan"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
db=SQLAlchemy(app)
bootstrap=Bootstrap(app)
login=LoginManager(app)
login.login_view="sing_in"
#init_app(app)




if __name__ == "__main__":
    app.run(debug=-True)

    from app import routes, models
