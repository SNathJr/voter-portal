# Import python libraries
import os
import datetime

# Import flask specific libraries
from flask import Flask, flash, render_template, redirect, request, url_for, session
from flask_session import Session
from flask_bcrypt import generate_password_hash, check_password_hash

# Import SQLAlchemy db model
from models import *

# cloudinary imports for image CDN
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

# Create a flask application
app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Check for environment variable DATABASE_URL
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Check for environment variable CLOUDINARY_URL
if not os.getenv("CLOUDINARY_URL"):
    raise RuntimeError("CLOUDINARY_URL is not set")

# Set up database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)    # db as defined in models.py


# Function to check if the user is already logged in
# Browser specific
def already_logged_in():
    try:
        session['logged_in'] == True
    except KeyError:
        session['logged_in'] = False
    return session['logged_in']


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/login')
def login():
    return render_template("login.html")
