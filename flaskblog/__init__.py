from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
db = SQLAlchemy(app)

from flaskblog import routes

'''
As of version SQLAlchemy 3.0 to create your db file you will need to run some commands like this in the shell :
from flaskblog import app, db
app.app_context().push()
db.create_all()
db.session.add()
db.session.commit()
db.drop_all()
db.create_all()
User.query.all()
Post.query.all()
'''
