'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Students:
Brady Lamson, Emerson Hatton, Riley Moen, Ebenezer Addei, Eduardo Salinas
Description: motaverse - Models for the SQLAlchemy application
'''
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

    liked_posts = db.relationship('Post',
                                  secondary='post_likes',
                                  back_populates='likes')


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.String)

    # Change likes to be a relationship with the User model
    likes = db.relationship('User',
                            secondary='post_likes',
                            back_populates='liked_posts')

    user = db.relationship('User', back_populates='posts')


# Create a new table to represent the many-to-many relationship
# between users and liked posts
post_likes = db.Table(
    'post_likes',
    db.Column('user_id', db.Integer,
              db.ForeignKey('users.id'), primary_key=True),
    db.Column('post_id', db.Integer,
              db.ForeignKey('posts.id'), primary_key=True)
)

'''
class Comment(db.Model, UserMixin):
    __tablename__ = 'comments'
    user = db.relationship('User', back_populates='name', primary_key=True)
    content = db.Column(db.String)
'''
