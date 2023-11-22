import mysql.connector

class User():
    def __init__(self, userid, Pass, fname, lname, email, dob, pronouns):
        self.userid = userid
        self.Pass = Pass
        self.fname = fname
        self.lname = lname
        self.


class Journal():
    def __init__(self, jid, eid, jname, content):
        self.jid = jid
        self.eid = eid
        self.jname = jname
        self.content = content

class Emotion():
    def __init__(self, emotionid, emotion, emoji):
        self.emotionid = emotionid
        self.emotion = emotion
        self.emoji = emoji

class Advice():
    def __init__(self, aid, eid, aname, link, alt):
        self.aid = aid
        self.eid = eid
        self.aname = aname
        self.link = link
        self.alt = alt

class Exercise():
    def __init__(self, exid, eid, exname, link, alt):
        self.exid = exid
        self.eid = eid
        self.exname = exname
        self.link = link
        self.alt = alt

class Database():
    def __init__(self):
        self.db = mysql.connector.connect(
            host="jeremymark.ca",
            user="jeremy",
            password="jeremy",
            port=3306,
            database="MindNBody"
        )

    def get_emotions(self):
        query = "SELECT * FROM Emotions;"

        cursor = self.db.cursor()
        cursor.execute(query)

        result = cursor.fetchall()

        emotions = []

        for row in result:
            emotion = Emotion(row[0], row[1], row[2])
            emotions.append(emotion)
        
        return emotions

    def get_emotion_emotion(self, eid: int):
        emotions = self.get_emotions()
        for emotion in emotions:
            if emotion.emotionid == eid:
                return emotion.emotion
        return None
    
    def get_emotion_emoji(self, eid: int):
        emotions = self.get_emotions()
        for emotion in emotions:
            if emotion.emotionid == eid:
                return emotion.emoji
        return None

    def insert_raw_journal(self, eid: int, jname: str, content: str) -> int:
        cursor = self.db.cursor()
        query = "INSERT INTO Journal (eid, jname, content) VALUES ("+ str(eid) + ", \"" + str(jname) + "\", \"" + str(content) + "\");"
        cursor.execute(query)

        self.db.commit()
        jid = cursor.lastrowid

        return jid

    def insert_journal(self, userid: int, eid: int, jname: str, content: str) -> int:
        jid = self.insert_raw_journal(eid, jname, content)
        
        query = "INSERT INTO JLibrary (jid, userid) VALUES (" + str(jid) + "," + str(userid) + ");"
        cursor = self.db.cursor()
        cursor.execute(query)
        self.db.commit()

        return jid
    
    def get_journal_by_id(self, jid: int) -> Journal:
        query = "SELECT * FROM Journal WHERE jid = " + str(jid) + ";"
        cursor = self.db.cursor()
        cursor.execute(query)

        result = cursor.fetchall()
        if(len(result) == 1):
            jt = result[0]
            return Journal(int(jt[0]), int(jt[1]), jt[2], jt[3])
        return None
    
    # Get the list of advices given a particular eid
    def get_advices(self, eid: int):

        query = "SELECT * FROM Advices WHERE eid = " + str(eid) + ";"
        cursor = self.db.cursor()
        cursor.execute(query)

        advices = []

        result = cursor.fetchall()

        for a in result:
            advice = Advice(int(a[0]), int(a[1]), a[2], a[3], a[4])
            advices.append(advice)

        return advices

    # Get the list of exercises given a particular eid
    def get_exercises(self, eid: int):
        query = "SELECT * FROM Exercises WHERE eid = " + str(eid) + ";"
        cursor = self.db.cursor()
        cursor.execute(query)

        exercises = []

        result = cursor.fetchall()

        for exer in result:
            exercise = Exercise(int(exer[0]), int(exer[1]), exer[2], exer[3], exer[4])
            exercises.append(exercise)

        return exercises

    # Get a list of journal ids ([1, 2, 3,..]) given a userid (e.g. 3)
    def get_all_journal_ids(self, userid: int):
        query = "SELECT * FROM JLibrary WHERE userid=" + str(userid) + ";"
        cursor = self.db.cursor()
        cursor.execute(query)

        result = cursor.fetchall()

        journal_ids = []

        for a in result:
            journal_ids.append(a[0])

        return journal_ids
    
    def get_all_users(self):


    

if __name__ == '__main__':
    database = Database()

    # Example 1 : Getting emotions from database
    print("\n\nExample 1\n\n")
    emotions = database.get_emotions()
    for e in emotions:
        mystr = "(" + str(e.emotionid) + ", " + str(e.emotion) + ", " + str(e.emoji) + ")"
        print(mystr)

    # Example 2 : Inserting a happy journal into Journal table
    print("\n\nExample 2\n\n")
    # 2a. Get the emotionid for `hap`
    emotionid = -1 # we want to find the `happy` emotionid
    for e in emotions:
        if e.emotion == "hap":
            emotionid = e.emotionid

    # 2b. Insert it into database
    userid = 3
    if emotionid != -1:
        # we are guaranteed that `emotionid` is the happy emotionid
        jname = "I am so happy"
        content = "I had ice cream today"
        jid = database.insert_journal(userid, emotionid, jname, content)
        print("Inserted (%s, %s, %s, %s) into Journal" %(str(jid), str(emotionid), jname, content))
        print("Inserted (%s, %s) into JLibrary" %(str(jid), str(userid)))

    # Example 3 : Get advice from a particular eid
    print("\n\nExample 3\n\n")
    emotionid = 2
    advices = database.get_advices(emotionid)
    for advice in advices:
        print(str(advice.aid) + ": " + advice.aname + " | " + advice.link)

    # Example 4 : Get exercises from a particular eid
    print("\n\nExample 4\n\n")
    emotionid = 3
    exercises = database.get_exercises(emotionid)
    for exercise in exercises:
        print(str(exercise.exid) + ": \"" + str(database.get_emotion_emoji(emotionid)) + "\" means you should do exercise: " + str(exercise.exname) + ": (" + str(exercise.link) + ")")

    # Example 5 : Get all the journal ids from a userid
    print("\n\nExample 5\n\n")
    userid = 3
    journal_ids = database.get_all_journal_ids(userid)
    print(str(journal_ids))

    # Example 6: Get Journal by id == 1
    jid = 1
    journal = database.get_journal_by_id(jid)
    print("Journal: (%s, %s, %s, %s)" %(str(journal.jid), str(journal.eid), journal.jname, journal.content))
