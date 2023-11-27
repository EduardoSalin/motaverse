from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    type = db.Column(db.String(50))

    name = db.Column(db.String)
    profile_picture = db.Column(db.String(120))

    passwd = db.Column(db.LargeBinary)
    #email = db.Column(db.String) #*****delete later
    #creation_date = db.Column(db.String)#*****delete later




    # Polymorphic relationship
    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "user"
    }

    #orders = db.relationship('Order', back_populates='user')

class Admin(User):
    title = db.Column(db.String)
    #name = db.Column(db.String(50))

    # Polymorphic identity for Admin
    __mapper_args__ = {
        "polymorphic_identity": "admin"
    }

'''
    *** This should be implemented for later user stories ***
    
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')
    blocked_users = db.relationship('User', secondary=blocked, lazy='subquery',
                                    backref=db.backref('blocked_by', lazy=True))
'''
'''
class Reseller(User):
    company = db.Column(db.String)
    address = db.Column(db.String)
    phone_number = db.Column(db.String)
    website = db.Column(db.String)

    # Polymorphic identity for Reseller
    __mapper_args__ = {
        "polymorphic_identity": "reseller"
    }
'''