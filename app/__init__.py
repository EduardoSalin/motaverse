from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import bcrypt
import os
'''
template_folder: path to the templates folder
static_folder: path to the static folder
'''
app = Flask(
    "Authentication Web App",
    template_folder=os.path.join(os.path.dirname(__file__), 'templates'), 
    static_folder='app/static'
    
)

    
app.config['SECRET_KEY'] = 'the quick brown dog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# db initialization
db = SQLAlchemy(app)

# login manager
login_manager = LoginManager()
login_manager.init_app(app)


from app.models import User, Admin

with app.app_context():
    db.create_all()

'''
This is where you will input your data. 
*id is what you will be using to login
*passwd is the password, obviously
*name is what will be displayed on the website
***
profile_picture is the path to the profile picture, if you want a default one, just name it picx.png where x = 1 to 8
if you want to add a profile picture, put the image in app/static/pic and write the name here
I found that it only really works with .jpg files, so I would recommend using that, 
if you have a png I found that you can just rename it to .jpg and it will work
***
leave title as admin, idk what it does but it works
'''

admins_to_add = [
    {'id': 'tmota', 'passwd': '1', 'name': 'Thaygo Mota', 'title': 'Admin'},
    {'id': 'e', 'passwd': '1', 'name': 'ES', 'profile_picture': 'picz.jpg', 'title': 'Admin'},
    {'id': 'b', 'passwd': '1', 'name': 'BL', 'profile_picture': 'pic3.jpg', 'title': 'Admin'}
    #{'id': 'x', 'passwd': '1', 'name': 'a', 'profile_picture': 'pic1.jpg', 'title': 'Admin'}
    #{'id': 'y', 'passwd': '1', 'name': 'a', 'profile_picture': 'pic1.jpg', 'title': 'Admin'}
    #{'id': 'z', 'passwd': '1', 'name': 'a', 'profile_picture': 'pic1.jpg', 'title': 'Admin'}
]

# Check and add admin users
with app.app_context():
    for admin_data in admins_to_add:
        admin_id = admin_data['id']
        # Check if the admin with the given ID already exists in the database
        existing_admin = Admin.query.get(admin_id)
        
        # If the admin doesn't exist, add it to the database
        if not existing_admin:
            # Hash the password using bcrypt
            password = admin_data['passwd'].encode('utf-8')
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            
            admin_data['passwd'] = hashed_password
            
            admin = Admin(**admin_data)
            db.session.add(admin)
    
    # Commit the admin user additions
    db.session.commit()


# user_loader callback
@login_manager.user_loader
def load_user(id):
    try: 
        return db.session.query(User).filter(User.id==id).one()
    except: 
        return None

from app import routes
