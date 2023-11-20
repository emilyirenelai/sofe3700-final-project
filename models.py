#mindfullness/models.py

from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    pass_field = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    dob = models.DateField()
    pronouns = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Journal(models.Model):
    jid = models.AutoField(primary_key = True)
    eid = models.IntegerField()
    jname = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.jname

class JLibrary(models.Model):
    jid = models.AutoField(primary_key = True)
    jname = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.jname

class Emotions(models.Model):
    emotion_id = models.AutoField(primary_key = True)
    emotion = models.CharField(max_length=50)
    emoji = models.IntegerField()

    def __str__(self):
        return self.emotion

class Exercises(models.Model):
    ex_id = models.AutoField(primary_key = True)
    eid = models.IntegerField()
    ex_name = models.CharField(max_length = 50)
    link = models.CharField(max_length = 50)
    alt = models.CharField(max_length = 50)

    def __str__(self):
        return self.ex_name

class Advices(models.Model):
    aid = models.AutoField(primary_key =True)
    eid = models.IntegerField()
    aname = models.CharField(max_length = 50)
    link = models.CharField(max_length = 50)
    alt = models.CharField(max_length = 50)

    def __str__(self):
        return self.aname

class Music(models.Model):
    m_id = models.AutoField(primary_key = True)
    eid = models.IntegerField()
    mname = models.CharField(max_length = 50)
    link = models.CharField(max_length = 50)
    alt = models.CharField(max_length = 50)

    def __str__(self):
        return self.mname

