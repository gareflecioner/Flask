import math
import sqlite3
import time
from flask import Flask, render_template, request, redirect, url_for, flash, g, session
from flask_bootstrap import Bootstrap
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///base.db"
app.config["SECRET_KEY"]="secret_key_i_love-attack-on-titan"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
db=SQLAlchemy(app)
bootstrap=Bootstrap(app)


class User(UserMixin, db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False,unique=True)
    password = db.Column(db.String(50), nullable=False)
    Created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id

class registration(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    feedback = db.Column(db.String(50), nullable=False)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<registration %r>' % self.id


class vinyl(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)


    def __repr__(self):
        return '<vinyl %r>' % self.id


class papers(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    market = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return '<papers %r>' % self.id

@app.route("/profile")
def my_profile():
    return render_template("profile.html")


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/feedback", methods=["POST", "GET"])
def feed():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        feedback = request.form["feedback"]
        wishes = registration(name=name, email=email, feedback=feedback)

        try:
            db.session.add(wishes)
            db.session.commit()
            return redirect("/wishes")
        except:
            "Sorry"
    else:
        return render_template("feedback.html")

@app.route("/login", methods=["POST", "GET"])
def sing_in():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('psw')
        remember = True if request.form.get('remember') else False
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Please try again')
            return redirect('/login')
        else:
            return redirect('/profile')
            return render_template("profile.html")
    else:
        return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def registration():
    if request.method == "POST":
        session.pop('_flashes', None)
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["psw"]
        password2 = request.form["psw2"]
        if len(name) > 4 and len(email) > 4 and len(password) > 4 and password == password2 :
            hash = generate_password_hash(request.form["psw"])
            res = User(name=name, email=email, password=hash)
            try:
                db.session.add(res)
                db.session.commit()
                return redirect('/login')
            except:
                flash("Ошибка при добавлении пользователя")
        else:
            flash('Ошибка в заполнении форм')
            return redirect('/register')
    else:
        return render_template("registration.html")


@app.route("/wishes")
def wish():
    back = registration.query.order_by(registration.datetime.desc()).all()
    return render_template("wish.html", back=back)


@app.route("/comment/<int:id>")
def comments(id):
    comment = registration.query.get(id)
    return render_template("comment.html", comment=comment)


@app.route("/pricing")
def pricing():
    return render_template("pricing.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/papers")
def books():
    pap = papers.query.order_by(papers.id).all()
    return render_template("papers.html", pap=pap)


@app.route("/paper/<int:id>")
def book(id):
    papp = papers.query.get(id)
    return render_template("paper.html", papp=papp)


@app.route("/records")
def records():
    rec = vinyl.query.order_by(vinyl.id.desc()).all()
    return render_template("records.html", rec=rec)


@app.route("/record/<int:id>")
def record(id):
    recordd = vinyl.query.get(id)
    return render_template("record.html", recordd=recordd)


if __name__ == "__main__":
    app.run(debug=-True)