from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    jname = StringField('Journal Name: ')
    content = StringField('Content: ')
    submit = SubmitField('Add')
    
class LoginForm(FlaskForm):
    email = StringField('Email: ')
    password = StringField('Password: ')
    submit = SubmitField('Login')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Journal Entry to Remove:')
    submit = SubmitField('Remove')

class WriteForm():
    jname = StringField('JName: ')
