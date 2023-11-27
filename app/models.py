from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    type = db.Column(db.String(50))
    name = db.Column(db.String)
    profile_picture = db.Column(db.String(120))
    passwd = db.Column(db.LargeBinary)

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