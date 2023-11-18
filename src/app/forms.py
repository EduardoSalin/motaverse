from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
from datetime import date

class SignUpForm(FlaskForm):
    id = StringField('Id', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    company = StringField('Company Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    website = StringField('Website', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    passwd_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')
    
class AdminSignUpForm(FlaskForm):
    id = StringField('Admin ID', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    passwd_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class SignInForm(FlaskForm):
    id = StringField('Id', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class LoginForm(FlaskForm):
    id = StringField('Username', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

