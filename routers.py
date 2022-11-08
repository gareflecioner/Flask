from flask import Flask, render_template, request, redirect, url_for, flash, g, session
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from models import User,registration,vinyl,papers
from forms import RegistrationForm,LoginForm,FeedForm
from init import db,app



@app.route("/logout")
#@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route("/profile/<name>")
#@login_required
def my_profile(name):
    name=User.query.filter_by(name=name).first_or_404()
    posts=[
        {'Author: ' user,'body' : 'test1}
    ]
    return render_template("profile.html",name=current_user.name)

@app.route("/index")
#@login_required
def index():
    return render_template("index.html")



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
    if current_user.is_authenticatred:
        return redirect(url_for("index"))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')

        return redirect(url_for('sing_in'))
        login_user(user, remember=form.remember_me.data)
    return redirect(url_for("index"))
    return render_template('login.html',form=form)



@app.route("/register", methods=["POST", "GET"])
def registration():    
    if current_user.is_authenticatred:
       return redirect(url_for("index"))
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(name=form.name.data,email=form.email.data)
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('All ok,you are logged up)
            return redirect(url_for('sing_in'))
                  
          except:
              flash("Ошибка при добавлении пользователя")
                  
     return render_template("registration.html",form=form)
    
   
@app.route("/wishes")
def wish():
    back = registration.query.order_by(registration.datetime.desc()).all()
    return render_template("wish.html", back=back)


@app.route("/comment/<int:id>")
#@login_required
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
#@login_required
def book(id):
    papp = papers.query.get(id)
    return render_template("paper.html", papp=papp)


@app.route("/records")
def records():
    rec = vinyl.query.order_by(vinyl.id.desc()).all()
    return render_template("records.html", rec=rec)


@app.route("/record/<int:id>")
#@login_required
def record(id):
    recordd = vinyl.query.get(id)
    return render_template("record.html", recordd=recordd)
