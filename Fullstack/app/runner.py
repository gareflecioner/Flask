import os
from __init__ import app,db
from flask_script import Manager,Shell

manager=Manager(app)

def make_shell_context():
    return dict(app=app, db=db, User=User, registration=registration,vinyl=vinyl, papers=papers)

manager.add_command('shell',Shell(make_context=make_shell_context))
manager.add_command('db')

if __name__ == "__main__":
    manager.run(debug=-True,use_reloader=False)