from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    username = db.Column(db.String, primary_key=True)
    email = db.Column(db.String)
    passwd = db.Column(db.LargeBinary)

class Post(db.Model, UserMixin):
    __tablename__ = 'posts'
    user = db.relationship('User', back_populates='username', primary_key=True)
    content = db.Column(db.String)
    likes = db.Column(db.Integer)
    comments = db.relationship('Comment', back_populates='')

class Comment(db.Model, UserMixin):
    __tablename__ = 'comments'
    user = db.relationship('User', back_populaes='username', primary_key=True)
    content = db.Column(db.String)