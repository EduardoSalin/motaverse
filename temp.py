from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired

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
    '''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Students: 
Brady Lamson, Emerson Hatton, Riley Moen, Ebenezer Addei, Eduardo Salinas
Description: motaverse - Forms for the SQLAlchemy application
'''
py -m pycodestyle app/models.py