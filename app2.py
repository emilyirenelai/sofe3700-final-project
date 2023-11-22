import os
import time
from flask import Flask, render_template, redirect, url_for
from forms import AddForm, DelForm
from newapp import Database
from cohere_mood_training import get_emotion

time.clock = time.time
app = Flask (__name__)
# secret key for forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################ Forms ##############################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    form = AddForm()

    if form.validate_on_submit():
        userid = form.userid.data
        jname = form.jname.data
        content = form.content.data
        emotion = get_emotion(content)  # Assuming get_emotion returns the emotion based on content
        print('AI: %s' %emotion)
        eid = -1
        emotions = Database().get_all_emotions()
        for em in emotions:
            if em.emotion == emotion:
                eid = em.emotionid
                break
        if eid != -1:
            jid = Database().insert_journal(userid, eid, jname, content)
            print('jid: %s' %str(jid))
        # Perform the necessary actions with the data, for example, store it in a database

        # return redirect(url_for('home.html'))  # Redirect to the index page after successful form submission
    else:
        print(form.errors)
    return render_template('add.html',form=form)

#################### TODO: Dynamically assign Jname ##############
@app.route('/list')
def list_entries():
    entries = Database().get_all_entries()  # Replace with method to get entries from the database
    return render_template('list.html', entries=entries)

@app.route('/delete', methods=['GET', 'POST'])
def del_entry():
    pass

if __name__ == '__main__':
    app.run(debug=True)