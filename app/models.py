from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    type = db.Column(db.String(50))
    name = db.Column(db.String)
    profile_picture = db.Column(db.String(120))
    passwd = db.Column(db.LargeBinary)
    posts = db.relationship('Post', back_populates='user', lazy=True)

    # Polymorphic relationship
    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "user"
    }


class Admin(User):
    title = db.Column(db.String)

    # Polymorphic identity for Admin
    __mapper_args__ = {
        "polymorphic_identity": "admin"
    }


class Post(db.Model, UserMixin):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.String)
    likes = db.Column(db.Integer)

    user = db.Relationship('User', back_populates='posts')
    # comments = db.relationship('Comment', back_populates='')

'''
class Comment(db.Model, UserMixin):
    __tablename__ = 'comments'
    user = db.relationship('User', back_populates='name', primary_key=True)
    content = db.Column(db.String)
'''