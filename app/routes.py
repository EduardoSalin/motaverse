from app import app, db, load_user
from app.models import User, Admin
from app.forms import *
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, logout_user, current_user
import bcrypt

@app.route('/')
@app.route('/index')
@app.route('/index.html')

def index():
    return render_template('index.html')

@app.route('/user/signup', methods=['GET', 'POST'])
def user_signup():
    form = SignUpForm()
    
    if form.validate_on_submit():
        passwd = form.passwd.data
        passwd_confirm = form.passwd_confirm.data
        
        # Check if passwords match
        if passwd != passwd_confirm:
            return '<p>Passwords do not match</p>'
        
        # Hash the password
        hashed = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
        
        # Check if a user with the given ID already exists
        existing_user = User.query.filter_by(id=form.id.data).first()
        if existing_user:
            return '<p>User with this ID already exists!</p>'
        
        # Create a new user
        new_user = User(
            id=form.id.data,
            name=form.name.data,
            profile_picture=form.profile_picture.data,
            passwd=hashed
        )
        
        # Add the new user to the database and commit
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('index'))
    
    return render_template('user_signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Replace with the actual form you're using for login

    if form.validate_on_submit():
        id = form.id.data
        passwd = form.passwd.data

        # Determine user type based on credentials
        admin = Admin.query.filter_by(id=id).first()
        user = User.query.filter_by(id=id).first()

        if admin and bcrypt.checkpw(passwd.encode('utf-8'), admin.passwd):
            # Admin login successful
            login_user(admin)
            flash('Admin login successful', 'success')
            return redirect(url_for('motaverse'))
        elif user and bcrypt.checkpw(passwd.encode('utf-8'), user.passwd):
            # User login successful
            login_user(user)
            flash('User login successful', 'success')
            return redirect(url_for('motaverse'))
        else:
            flash('Invalid ID or password', 'danger')

    return render_template('login.html', form=form)


# This will log out the user and remove their information from the session
@app.route('/user/signout')
def user_signout():
    logout_user()  
    return redirect(url_for('index'))

@app.route('/user/signout')
def admin_signout():
    logout_user()  
    return redirect(url_for('index'))

@app.route('/motaverse')
@login_required
def motaverse():
    profile_picture = url_for('static', filename='pic/' + current_user.profile_picture)
    return render_template('motaverse.html', profile_picture=profile_picture)

    # You can fetch posts and profiles from the database if you have them.
    # For now, we'll pass placeholders to the template.