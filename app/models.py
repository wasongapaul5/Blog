from . import db
from datetime import datetime
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash

from app import login_manager

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), nullable=True, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    image_file = db.Column(db.String(255), nullable=False, default='default.jpg')
    posts = db.relationship('post', backref='author',lazy=True)
    comment = db.relationship('Comment', backref='author',lazy=True)
    




    