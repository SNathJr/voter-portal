# import libraries
import datetime
from flask_sqlalchemy import SQLAlchemy

# setup a database connection with SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    middlename = db.Column(db.String(100))
    lastname = db.Column(db.String(100), nullable=False)
    emailid = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    verified = db.Column(db.Boolean, nullable=False)
    voters = db.relationship("Voter", backref="users", lazy=True)

class Voter(db.Model):
    __tablename__ = 'voters'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    photo = db.Column(db.String(200), unique=True, nullable=False)
    father_name = db.Column(db.String(200), nullable=False)
    sex = db.Column(db.Boolean, nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    address = db.Column(db.String(500), nullable=False)