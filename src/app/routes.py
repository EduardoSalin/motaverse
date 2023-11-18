from app import app, db, load_user
from app.models import User,Reseller, Admin
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
        new_user = Reseller(
            id=form.id.data,
            name=form.name.data,
            email=form.email.data,
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
        reseller = Reseller.query.filter_by(id=id).first()

        if admin and bcrypt.checkpw(passwd.encode('utf-8'), admin.passwd):
            # Admin login successful
            login_user(admin)
            flash('Admin login successful', 'success')
            return redirect(url_for('motaverse'))
        elif reseller and bcrypt.checkpw(passwd.encode('utf-8'), reseller.passwd):
            # Reseller login successful
            login_user(reseller)
            flash('Reseller login successful', 'success')
            return redirect(url_for('motaverse'))
        else:
            flash('Invalid ID or password', 'danger')

    return render_template('login.html', form=form)


# This will log out the user and remove their information from the session
@app.route('/user/signout')
def reseller_signout():
    logout_user()  
    return redirect(url_for('index'))

@app.route('/user/signout')
def admin_signout():
    logout_user()  
    return redirect(url_for('index'))

@app.route('/motaverse')
@login_required
def motaverse():
    # You can fetch posts and profiles from the database if you have them.
    # For now, we'll pass placeholders to the template.
    return render_template('motaverse.html')




'''
#Admin

@app.route('/admin/signin', methods=['GET', 'POST'])
def admin_signin():
    form = SignInForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(id=form.id.data).first()
        if admin and bcrypt.checkpw(form.passwd.data.encode('utf-8'), admin.passwd):
            login_user(admin)
            return redirect(url_for('motaverse')) 
        else:
            return '<p>Invalid ID or password</p>'
    return render_template('admin_signin.html', form=form)



@app.route('/admin/signup', methods=['GET', 'POST'])
def admin_signup():
    form = AdminSignUpForm()
    if form.validate_on_submit():
        passwd = form.passwd.data
        passwd_confirm = form.passwd_confirm.data
        if passwd != passwd_confirm:
            return '<p>Passwords do not match</p>'
        
        # Hash the password
        hashed = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
        
        # Check if an admin with the given ID already exists
        existing_admin = Admin.query.filter_by(id=form.id.data).first()
        if existing_admin:
            return '<p>Admin with this ID already exists!</p>'
        
        # Create a new admin
        new_admin = Admin(
            id=form.id.data,
            passwd=hashed
        )
        
        # Add the new admin to the database and commit
        db.session.add(new_admin)
        db.session.commit()
        
        return redirect(url_for('index'))
    
    return render_template('admin_signup.html', form=form)
'''
'''
#This was used in project 1, we probablily won't need it, delete later
@app.route('/reseller/signin', methods=['GET', 'POST'])
def reseller_signin():
    form = SignInForm()
    if form.validate_on_submit():
        # Check if user exists
        user = Reseller.query.filter_by(id=form.id.data).first()
        #checking if user exists
        if not user:
            return '<p>Invalid ID or password</p>'
        #checking password at sign in
        if bcrypt.checkpw(form.passwd.data.encode('utf-8'), user.passwd):
            login_user(user)
            return redirect(url_for('orders'))
        else:
            return '<p>Invalid ID or password</p>'

    
    return render_template('reseller_signin.html', form=form)
'''




