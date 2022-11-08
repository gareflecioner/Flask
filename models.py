import math
import sqlite3
import time
from flask import Flask, render_template, request, redirect, url_for, flash, g, session
from flask_bootstrap import Bootstrap
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False,unique=True)
    password = db.Column(db.String(50), nullable=False)
    Created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self,password):
        self.password_hash=generate_password_hash(password)
        
    def check_password(self,password):
        return check_password_hash(self.password.hash,password)

    def __repr__(self):
        return '<User %r>' % self.id
    
#db with wishes
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

