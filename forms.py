from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    userid = IntegerField('User ID: ')
    jname = StringField('Journal Name: ')
    content = StringField('Content: ')
    submit = SubmitField('Add')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Journal Entry to Remove:')
    submit = SubmitField('Remove')
