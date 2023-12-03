'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Students:
Brady Lamson, Emerson Hatton, Riley Moen, Ebenezer Addei, Eduardo Salinas
Description: motaverse - Models for the SQLAlchemy application
'''
from flask_login import UserMixin
from app import db

user_blocklist = db.Table(
    'user_blocklist',
    db.Column('user_id', db.String, db.ForeignKey('users.id'), primary_key=True),
    db.Column('blocked_user_id', db.String, db.ForeignKey('users.id'), primary_key=True)
)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    type = db.Column(db.String(50))
    name = db.Column(db.String)
    profile_picture = db.Column(db.String(120))
    passwd = db.Column(db.LargeBinary)
    posts = db.relationship('Post', back_populates='user', lazy=True)
    comments = db.relationship('Comment', back_populates='user', lazy=True)

    # Polymorphic relationship
    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "user"
    }

    liked_posts = db.relationship(
        'Post',
        secondary='post_likes',
        back_populates='likes'
    )
    
    blocked_users = db.relationship(
        'User',
        secondary=user_blocklist,
        primaryjoin=(user_blocklist.c.user_id == id),
        secondaryjoin=(user_blocklist.c.blocked_user_id == id),
        back_populates='blocking_users'
    )

    blocking_users = db.relationship(
        'User',
        secondary=user_blocklist,
        primaryjoin=(user_blocklist.c.blocked_user_id == id),
        secondaryjoin=(user_blocklist.c.user_id == id),
        back_populates='blocked_users'
    )

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.String)
    comments = db.relationship('Comment', back_populates='post', lazy=True)

    likes = db.relationship(
        'User',
        secondary='post_likes',
        back_populates='liked_posts'
    )

    user = db.relationship('User', back_populates='posts')

    def count_likes(self):
        return len(self.likes)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    content = db.Column(db.String)

    # Establish a relationship with the User model for the comment author
    user = db.relationship('User', back_populates='comments')

    # Establish a relationship with the Post model for the associated post
    post = db.relationship('Post', back_populates='comments')

# Create a new table to represent the many-to-many relationship
# between users and liked posts

post_likes = db.Table(
    'post_likes',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True)
)

