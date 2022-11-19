import math
import os.path
import sqlite3
import time
from flask import Flask, render_template, request, redirect, url_for, flash, g, session
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from FDataBase import FDataBase


DATABASE="/tmp/flaskdb.db"
DEBUG=True
SECRET_KEY="cf62789osl.hnm,a,.lk256789ioql2,.s;p"
USERNAME="admin"
PASSWORD='123'

app=Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path,"flaskdb.db")))

dbase=None
@app.before_request
def before_request():
    global dbase
    db=get_db()
    dbase=FDataBase()

def connect_db():
    conn=sqlite3.connect(app.config["DATABASE"])
    conn.row_factory=sqlite3.Row
    return conn

def create_db():
    db=connect_db()
    with app.open_resource("reg_db.sql",mode="r") as f:
        db.cursor().executescript(f.read())
        db.commit()
        db.close()


def get_db():
    if not hasattr(g,"link_db"):
        g.link_db=connect_db()
    return g.link_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,"link_db"):
        g.link_db.close()


@app.route("/")
def main():
    return render_template("main.html")

@app.route("/papers")
def books():
    return render_template("papers.html")

@app.route("/paper/<int:id>")
def book():
    return render_template("paper.html")

@app.route("/records")
def records():
    return render_template("records.html")


@app.route("/pricing")
def pricing():
    return render_template("pricing.html")




@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/feedback",methods=["POST","GET"])
def feed():
    if request.method =="POST":
        if len(request.form['name'])>4 and len(request.form['email'])>4 and len(request.form['text'])>5 :
            res=dbase.addPost(request.form['name'],request.form['email'],request.form['text'])
            if not res:
                flash('Ошибка в добавлении статьи')
            else:
                flash("Статья добавлена")

        else:
            flash("Неправильно заполнены поля")
    return render_template("feedback.html")


@app.route("/wishes")
def wish():

    return render_template("wish.html")



@app.route("/search")
def search():
    return render_template("search.html")




@app.route("/login")
def sing_in():
    return render_template("login.html")



@app.route("/register",methods=["POST","GET"])
def registration():
    if request.method=="POST":
        session.pop('_flashes:None')
        if (len(request.form["name"])>4 and len(request.form["email"])>4
            and len(request.form["psw"])>4 and request.form["psw"] == request.form["psw2"]):
            hash=generate_password_hash(request.form["psw"])
            res=dbase.addUser(request.form["name"],request.form["email"],hash)
            if res:
                return redirect('/login')
            else:
                flash("Ошибка при добавлении пользователя")
        flash('Ошибка в заполнении форм')

    return render_template("registration.html")


if __name__=="__main__":
    app.run(debug=-True)