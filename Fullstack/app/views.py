from __init__ import app
from flask import Flask, render_template, redirect, url_for, flash,request
from flask_login import UserMixin, LoginManager, login_user, logout_user, current_user, login_required
from .models import User,registration,vinyl,papers
from .forms import RegistrationForm,LoginForm,FeedForm

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route("/profile/<name>")
@login_required
def my_profile(name):
    username=User.query.filter_by(name=name).first_or_404()
    return render_template("profile.html",username=username)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/feedback", methods=["POST", "GET"])
@login_required
def feed():
    #if current_user.is_authenticated:
        #return redirect (url_for('sing_in'))
    form=FeedForm()
    if request.method=='POST':
    #form=FeedForm()
        if form.validate_on_submit():
            wishes = registration(name=form.name.data, email=form.email.data, feedback=form.feed.data)
            try:
                db.session.add(wishes)
                db.session.commit()
                flash('Сongratulations you left your review')
                return redirect(url_for('wish'))
            except Exception as a:
                print(str(a))
    return render_template('feedback.html',form=form)

@app.route("/login", methods=["POST", "GET"])
def sing_in():
    if current_user.is_authenticated:
        return redirect(url_for("sing_in"))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('sing_in'))
        login_user(user, remember=form.remember_me.data)
        next_page=request.args.get('next')
        if not next_page or url_parse(next_page).netlock != '':
            next_page=url_for('main')
            return redirect(next_page)
    return render_template('login.html',form=form)



@app.route("/register", methods=["POST", "GET"])
def reg():
    if current_user.is_authenticated:
       return redirect(url_for("sing_in"))
    form=RegistrationForm()
    if form.validate_on_submit():
        password=generate_password_hash(form.password.data)
        user=User(name=form.name.data,email=form.email.data,password=password)
        try:

            db.session.add(user)
            db.session.commit()

            return redirect(url_for('sing_in'))

        except TypeError :
            return db.session.rollback()

    return render_template("registration.html",form=form)
    
   
@app.route("/wishes")
@login_required
def wish():
    back = registration.query.order_by(registration.datetime.desc()).all()
    return render_template("wish.html", back=back)


@app.route("/comment/<int:id>")
@login_required
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
@login_required
def book(id):
    papp = papers.query.get(id)
    return render_template("paper.html", papp=papp)


@app.route("/records")
def records():
    rec = vinyl.query.order_by(vinyl.id.desc()).all()
    return render_template("records.html", rec=rec)


@app.route("/record/<int:id>")
@login_required
def record(id):
    recordd = vinyl.query.get(id)
    return render_template("record.html", recordd=recordd)
