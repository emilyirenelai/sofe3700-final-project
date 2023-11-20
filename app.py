import os
import time
time.clock = time.time
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask (__name__)
from forms import AddForm, DelForm
# secret key for forms
app.config['SECRET_KEY'] = 'mysecretkey'


######################### SQL: SQLAlchemy uses SQLite ####################
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)

# Users table
class User(db.Model):

    __tablename__ = 'users'

    userid = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.Text)
    fname = db.Column(db.Text)
    lname = db.Column(db.Text)
    email = db.Column(db.Text)
    dob = db.Column(db.Text)
    pronouns = db.Column(db.Text)
    libid = db.Column(db.Integer)

    def __init__(self, password, fname, lname, email, dob, pronouns, libid):
        self.password = password
        self.fname = fname
        self.lname = lname
        self.email = email
        self.dob = dob
        self.pronouns = pronouns
        self.libid = libid

    def __repr__(self):
        return f"User {self.userid} has info: password = {self.password}, fname = {self.fname}, lname = {self.lname}, email = {self.email}, dob = {self.email}, pronouns = {self.pronouns}, libid = {self.libid}"
    
# Journals table
class Journal(db.Model):

    __tablename__ = 'journals'

    jid = db.Column(db.Integer, primary_key=True)
    eid = db.Column(db.Integer)
    jname = db.Column(db.Text)
    content = db.Column(db.Text)

    def __init__(self, eid, jname, content):
        self.eid = eid
        self.jname = jname
        self.content = content

    def __repr__(self):
        return f"eid:{self.eid} jname:{self.jname} content:{self.content}"

# Libraries table
class Library(db.Model):

    __tablename__ = 'Jlibrary'

    libid = db.Column(db.Integer, primary_key=True)
    jid = db.Column(db.Integer, nullable=False)
    jname = db.Column(db.Text)
    userid = db.Column(db.Integer, nullable=False)

    def __init__(self, jid, jname, userid):
        self.jid  = jid
        self.jname = jname
        self.userid = userid

    def __repr__(self):
        return f"jid:{self.jid} jname:{self.jname} userid:{self.userid}"
    
# Emotions table
class Emotion(db.Model):

    __tablename__ = 'emotions'

    emotionid = db.Column(db.Integer, primary_key=True)
    emotion = db.Column(db.Text)
    emoji = db.Column(db.Integer)

    def __init__(self, emotion, emoji):
        self.emotion = emotion
        self.emoji = emoji

# Exercises table
class Exercise(db.Model):

    __tablename__ = 'exercises'

    exid = db.Column(db.Integer, primary_key=True)
    eid = db.Column(db.Integer, nullable=False)
    exname = db.Column(db.Text)
    link = db.Column(db.Text)
    alt = db.Column(db.Text)

    def __init__(self, eid, exname, link, alt):
        self.eid = eid
        self.exname = exname
        self.link = link
        self.alt = alt
    
# Musics table
class Music(db.Model):

    __tablename__ = 'musics'

    mid = db.Column(db.Integer, primary_key=True)
    eid = db.Column(db.Integer, nullable=False)
    mnane = db.Column(db.Text)
    link = db.Column(db.Text)
    alt = db.Column(db.Text)

    def __init__(self, eid, mname, link, alt):
        self.eid = eid
        self.mname = mname
        self.link = link
        self.alt = alt

# Advices table
class Advice(db.Model):

    __tablename__ = 'advices'

    aid = db.Column(db.Integer, primary_key=True)
    eid = db.Column(db.Integer, nullable=False)
    aname = db.Column(db.Text)
    link = db.Column(db.Text)
    alt = db.Column(db.Text)

    def __init__(self, eid, aname, link, alt):
        self.eid = eid
        self.mname = aname
        self.link = link
        self.alt = alt

############################ Forms ##############################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        ############ TODO: Implement Cohere logic to determing Eid, and assign Jname based off user. #######
        # Add new Entry to database
        new_entry = Journal(1,'J7',name)
        db.session.add(new_entry)
        db.session.commit()

        return redirect(url_for('list_entries'))

    return render_template('add.html',form=form)

#################### TODO: Dynamically assign Jname ##############
@app.route('/list')
def list_entries():
    # List of entries from database.
    all_entries = Journal.query.all()
    return render_template('list.html', all_entries = all_entries)

@app.route('/delete', methods=['GET', 'POST'])
def del_entry():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        entry = Journal.query.get(id)
        db.session.delete(entry)
        db.session.commit()

        return redirect(url_for('list_entries'))
    return render_template('delete.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)