DROP TABLE IF EXISTS Advices;
DROP TABLE IF EXISTS Music;
DROP TABLE IF EXISTS Exercises;
DROP TABLE IF EXISTS JLibrary;
DROP TABLE IF EXISTS Journal;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Emotions;

CREATE TABLE Emotions
(emotionid int not null AUTO_INCREMENT,
emotion varchar(255) not null,
emoji varchar(255) not null,
PRIMARY KEY (emotionid) 
);

CREATE TABLE Users
(userid int not null AUTO_INCREMENT,
pass varchar(255) not null,
fname varchar(255) not null,
lname varchar(255) not null,
email varchar(255) not null,
dob varchar(255) not null,
pronouns varchar(255),
PRIMARY KEY (userid));

CREATE TABLE Journal
(jid int not null AUTO_INCREMENT,
eid int not null,
jname varchar(255) not null,
content TEXT,
PRIMARY KEY (jid),
FOREIGN KEY (eid) REFERENCES Emotions(emotionid)
);

CREATE TABLE JLibrary
(jid int not null,
userid int not null,
FOREIGN KEY (userid) REFERENCES Users(userid),
FOREIGN KEY (jid) REFERENCES Journal(jid)
);

CREATE TABLE Exercises
(exid int not null AUTO_INCREMENT,
eid int not null,
exname varchar(255) not null,
link varchar(255) not null,
alt varchar(255) not null,
PRIMARY KEY (exid),
FOREIGN KEY (eid) REFERENCES Emotions(emotionid)
);


CREATE TABLE Music
(mid int not null AUTO_INCREMENT,
eid int not null,
mname varchar(255) not null,
link varchar(255) not null,
alt varchar(255) not null,
PRIMARY KEY (mid),
FOREIGN KEY (eid) REFERENCES Emotions(emotionid)
);

CREATE TABLE Advices
(aid int not null AUTO_INCREMENT,
eid int not null,
aname varchar(255) not null,
link varchar(255) not null,
alt varchar(255) not null,
PRIMARY KEY (aid),
FOREIGN KEY (eid) REFERENCES Emotions(emotionid)
);

INSERT INTO Emotions (emotion, emoji) VALUES
("hap", ":)"),
("hyp", ":D"),
("sad", ":("),
("ang", ">:("),
("tir", "-.-"),
("neu", ":|");

INSERT INTO Users (pass, fname, lname, email, dob, pronouns) VALUES
("emily", "Emily", "Lai", "emily.lai1@ontariotechu.net", "2003/11/12","F"),
("alina", "Alina", "Mathew", "alina.mathew@ontariotechu.net", "2003/07/24", "F"),
("jonathan", "Jonathan", "Hua", "jonathan.hua@ontariotechu.net", "2000/06/02", "M"),
("natasha", "Natasha", "Naorem", "natasha.naorem@ontariotechu.net", "2002/12/28", "F"),
("hafeez", "Dr. Khalid Abdel", "Hafeez","khalid.hafeez@ontariotechu.ca", "1999/01/01", "M"),
("omar", "TA Omar", "Hemied", "omar.hemied@ontariotechu.net", "1999/01/02", "M"),
("asif", "TA Asif", "Khan", "asif.khan@ontariotechu.net", "1999/01/03", "M"),
("hossam", "Dean Hossam", "Kishawy", "hossam.kishawy@ontariotechu.net", "1998/01/01", "M"),
("steven", "President Steven", "Murphy", "steven.murphy@ontariotechu.net", "1998/01/02", "M"),
("john", "John", "Doe", "john.doe@ontariotechu.net", "1997/01/01", "M"),
("jane", "Jane", "Doe", "jane.doe@ontariotechu.net", "1997/01/02", "F");

INSERT INTO Journal (eid, jname, content) VALUES
(1, "Nov. 18, 2023: A Happy Day", "I was really happy since I got an A+ today on my Data Management Systems Final Project!"),
(3, "Nov. 19, 2023: I'm So Sad", "My boyfriend broke up with me for Wesley :(( Wes is just too much better than me."),
(4, "Nov. 20, 2023: Grr!", "Why does my professor have to assign so much homework?!"),
(6, "Nov. 21, 2023: Thoughts", "I took a long pause and thought about my future, and wondered if I could actually get a job better than McDonalds.");

INSERT INTO JLibrary (jid, userid) VALUES
(1, 1),
(2, 3),
(3, 1),
(4, 1);

INSERT INTO Exercises (eid, exname, link, alt) VALUES
(1, "Jump to it with a Jump Rope!", "https://www.youtube.com/watch?v=NfAJB_L3Q0k", "12 Minute Morning Jump Rope Workout"),
(1, "Get Strong with Calisthenics!", "https://www.youtube.com/watch?v=fWptOzJI3Wc", "30 Minute Calisthenics Full Body Workout"),
(2, "30 Minutes of Groovy Dancing!", "https://www.youtube.com/watch?v=QegSjK9Itbs", "30 Minute Groovy Dance Workout"),
(2, "1 Mile Happy Walk!", "https://www.youtube.com/watch?v=njeZ29umqVE&pp=ygUNaGFwcHkgd29ya291dA%3D%3D", "1 Mile Happy Walk"),
(3, "Walk for 1 hour", "https://www.youtube.com/watch?v=3MJlmMJVL2M&pp=ygUZR28gZm9yIGEgd2FsayBmb3IgYW4gaG91cg%3D%3D", "Walk for 1 hour a day"),
(3, "Motivate yourself with intense cardio!", "https://www.youtube.com/watch?v=eWjd8C2SB0Y&pp=ygUTaW50ZW5zZSBwb3Agd29ya291dA%3D%3D", "Intense 20 minute cardio"),
(4, "Build yourself to the ultimate strength!" ,"https://www.youtube.com/watch?v=DXg-lg3e8v0&pp=ygUddGhlIHVsdGltYXRlIHN0cmVuZ3RoIHdvcmtvdXQ%3D", "the ultimate strength workout"), 
(4, "Take your anger out on boxing", "https://www.youtube.com/watch?v=pWLEkO0MlXs&pp=ygUVa2ljayBib3hpbmcgMTUgbWludXRl", "15-minute boxing workout at home"),
(5, "Meditation requires no energy", "https://www.youtube.com/watch?v=hyg3abur5VI&pp=ygURbWVkaXRhdGlvbiAxIGhvdXI%3D", "1 hour meditation music"),
(5, "Breathing exercise for relaxation", "https://www.youtube.com/watch?v=7Ep5mKuRmAA&pp=ygUSYnJlYXRoaW5nIGV4ZXJjaXNl", "breathing"),
(6, "Beginner friendly workout", "https://www.youtube.com/watch?v=19G8775Qn9s&pp=ygUQcm91dGluZSBleGVyY2lzZQ%3D%3D", "morning workout"),
(6, "Run for fun!", "https://www.youtube.com/watch?v=v9XpWyvyadE&pp=ygUOcnVubmluZyAzMCBtaW4%3D", "30 minute run session");


INSERT INTO Music(eid, mname, link, alt) VALUES
(1, "Perfect Night by Le SSERAFIM", "https://www.youtube.com/watch?v=hLvWy2b857I&pp=ygUNcGVyZmVjdCBuaWdodA%3D%3D", "alt"),
(1, "Happy by Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs&pp=ygUOaGFwcHkgcG9wIHNvbmc%3D", "alt"),
(2, "The Beginning by ONE OK ROCK", "https://www.youtube.com/watch?v=hLvWy2b857I&pp=ygUNcGVyZmVjdCBuaWdodA%3D%3D", "alt"),
(2, "Let's Get It Started by The Black Eyed Peas", "https://www.youtube.com/watch?v=IKqV7DB8Iwg&list=PL10BZg10BCDQxKXg0qN_-Y6RwvfdDvJdy&index=1&pp=iAQB8AUB", "alt"),
(3, "Faded by Alan Walker", "https://www.youtube.com/watch?v=60ItHLz5WEA&list=PLKsiRyayPqRLqJsyEuuHx08yKkUDXv1cq&index=1&pp=iAQB8AUB", "alt"),
(3, "Happy Cat", "https://www.youtube.com/watch?v=hLvWy2b857I&pp=ygUNcGVyZmVjdCBuaWdodA%3D%3D", "alt"),
(4, "Funky Town", "https://www.youtube.com/watch?v=Z6dqIYKIBSU&pp=ygUKZnVua3kgdG93bg%3D%3D", "alt"),
(4, "Bad Blood by Taylor Swift ft. Kendrick Lamar", "https://www.youtube.com/watch?v=QcIy9NiNbmo&list=PLZtNd3NYxFfzaz63qQCjNGPLLF-5ESi_B&index=2&pp=iAQB8AUB", "alt"),
(5, "Blue Flame (Bass Cover)", "https://www.youtube.com/watch?v=dirfMzuRdn8&pp=ygUVYmFzcyBibHVlIGZsYW1lIGNvdmVy", "alt"),
(5, "See You Again by Wiz Khalifa ft. Charlie Puth", "https://www.youtube.com/watch?v=RgKAFK5djSk&list=RDQMaK14vmYyYq0&index=5&pp=8AUB", "alt"),
(6, "Uptown Funk by Mark Ronson ft. Bruno Mars", "https://www.youtube.com/watch?v=OPf0YbXqDm0&list=RDQMTFwbZhxmyWA&index=1&pp=8AUB", "alt"),
(6, "Some ZUTA MAYO Song Slap Bass Cover", "https://www.youtube.com/watch?v=SEbGu6J8scs&pp=ygUTc2xhcCBiYXNzIHp1dGEgbWF5bw%3D%3D", "alt");

INSERT INTO Advices (eid, aname, link, alt) VALUES
(1, "How to stay positive and retain your happy mindset", "https://www.nhs.uk/mental-health/self-help/tips-and-support/how-to-be-happier/", "alt"),
(1, "Create lasting happiness", "https://www.nhs.uk/mental-health/self-help/tips-and-support/how-to-be-happier/", "alt"),
(2, "It's okay to be super happy from time to time, but don't get used to it because we all die one day", "https://www.healthline.com/health/why-am-i-so-emotional-2", "alt"),
(3, "Sadness is good, because you are getting used to what most of life will feel like", "https://www.gundersenhealth.org/health-wellness/live-happy/healthy-ways-to-deal-with-sadness", "alt"),
(4, "How to control your anger", "https://www.nhsinform.scot/healthy-living/mental-wellbeing/anger-management/how-to-control-your-anger/", "alt"),
(5, "Self tips on fighting tiredness", "https://www.nhs.uk/live-well/sleep-and-tiredness/self-help-tips-to-fight-fatigue/", "alt"),
(6, "How to feel happier", "https://www.nhsinform.scot/healthy-living/mental-wellbeing/low-mood-and-depression/how-to-feel-happier/", "alt");
