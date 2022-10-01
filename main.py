from flask import Flask, render_template,request,redirect
from flask_bootstrap import Bootstrap

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///base.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS "]=False
db=SQLAlchemy(app)
bootstrap=Bootstrap(app)


class Registration(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Regisration %r>' % self.id



@app.route("/")
def main():
    return render_template("main.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

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
def papers():
    return render_template("papers.html")


@app.route("/records")
def records():
    return render_template("records.html")

if __name__=="__main__":
    app.run(debug=-True)