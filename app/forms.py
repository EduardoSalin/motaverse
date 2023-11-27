from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
from datetime import date

class SignUpForm(FlaskForm):
    id = StringField('Username', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    profile_picture = SelectField(
        'Profile Picture', 
        choices=[
            ('pic1.jpg', 'Picture 1'), 
            ('pic2.jpg', 'Picture 2'),
            ('pic3.jpg', 'Picture 3'),
            ('pic4.jpg', 'Picture 4'),
            ('pic5.jpg', 'Picture 5'),
            ('pic6.jpg', 'Picture 6'),
            ('pic7.jpg', 'Picture 7'),
            ('pic8.jpg', 'Picture 8')])
    
    passwd = PasswordField('Password', validators=[DataRequired()])
    passwd_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')
    
class AdminSignUpForm(FlaskForm):
    id = StringField('Admin ID', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    passwd_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class SignInForm(FlaskForm):
    id = StringField('Username', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class LoginForm(FlaskForm):
    id = StringField('Username', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class PostForm(FlaskForm):
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Comment')