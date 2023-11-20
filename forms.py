from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Content: ')
    submit = SubmitField('Add')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Journal Entry to Remove:')
    submit = SubmitField('Remove')
