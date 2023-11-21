from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    type = db.Column(db.String)
    email = db.Column(db.String)
    creation_date = db.Column(db.String)
    passwd = db.Column(db.LargeBinary)

    # Polymorphic relationship
    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "user"
    }

    #orders = db.relationship('Order', back_populates='user')

class Reseller(User):
    company = db.Column(db.String)
    address = db.Column(db.String)
    phone_number = db.Column(db.String)
    website = db.Column(db.String)

    # Polymorphic identity for Reseller
    __mapper_args__ = {
        "polymorphic_identity": "reseller"
    }

class Admin(User):
    title = db.Column(db.String)
    name = db.Column(db.String)

    # Polymorphic identity for Admin
    __mapper_args__ = {
        "polymorphic_identity": "admin"
    }
