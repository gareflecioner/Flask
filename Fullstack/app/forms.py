from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask_wtf import FlaskForm

class RegistrationForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    password2=PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sing up')

    def validate_name(self,name):
        user=User.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('Please use a different name')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different e-mail')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me=BooleanField("Remember me")
    submit=SubmitField("Sing in")

class FeedForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    feed=StringField("Feedback", validators=[DataRequired()])
    submit=SubmitField("Do it")
