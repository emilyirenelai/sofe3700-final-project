from app import db, User, Journal, Library, Emotion, Exercise, Music, Advice

# Creates all the tables
db.create_all()

jonhua = User('pass','Jonathan','Hua','jonathan.hua@ontariotechu.net','2000-06-02','M',1)
emilai = User('pass','Emily','Lai','emily.lai1@ontariotechu.net','1999-08-24','F',2)
alimat = User('pass','Alina','Mathew','alina.mathew@ontariotechu.net','2002-07-24','F',3)
natnao = User('pass','Natasha','Naorem','natasha.naorem@ontariotechu.net','2001-12-20','F',4)
drhaf = User('pass','Dr.','Hafeez','dr.hafeez@ontariotechu.net','2010-01-01','M',5)
bobthe = User('pass','Bob The','Builder','bobthebuilder@ontariotechu.net','1920-03-24','F',6)

db.session.add_all([jonhua,emilai,alimat,natnao,drhaf,bobthe])
db.session.commit()

j1 = Journal(1, 'J1', 'I was really happy since I got an A+ today!')
j2 = Journal(1, 'J2', 'My puppy died, I cried for 5 hours straight.')
j3 = Journal(1, 'J3', 'Why does my professor have to assign so much homework?!')
j4 = Journal(2, 'J4', 'I took a long pause and thought about my future, and wondered if I could actually get a job better than Mcdonalds.')
j5 = Journal(2, 'J5', 'I got 10/10 on my test and got ice cream as a reward!')
j6 = Journal(3, 'J6', 'Today I tripped on a rock and fell flat on my face in front of everyone, it was so embarrasing. It even got uploaded to TikTok!')

db.session.add_all([j1, j2, j3, j4, j5, j6])
db.session.commit()

jl1 = Library(1, 'J1', 1)
jl2 = Library(2, 'J2', 2)
jl3 = Library(3, 'J3', 3)
jl4 = Library(4, 'J4', 4)
jl5 = Library(5, 'J5', 5)
jl6 = Library(6, 'J6', 6)

db.session.add_all([jl1, jl2, jl3, jl4, jl5, jl6])
db.session.commit()

emo1 = Emotion('Happy',1)
emo2 = Emotion('Sad', 2)
emo3 = Emotion('Excited',3)
emo4 = Emotion('Moody',4)
emo5 = Emotion('emotion',5)
emo6 = Emotion('more emotion',6)

db.session.add_all([emo1, emo2, emo3, emo4, emo5, emo6])
db.session.commit()

ex1 = Exercise(1, 'Jump', 'https://www.youtube.com/watch?v=1UGS-ELqnu0', '15 MUST-DO Jumping Exercises for STRONG, POWERFUL Legs (and toned thighs)')
ex2 = Exercise(2, 'Sprint', 'https://www.youtube.com/watch?v=2YogM9wXAJg', 'HIIT vs HIRT | How to Do a Sprint Workout the RIGHT Way')
ex3 = Exercise(3, 'Jog', 'https://www.youtube.com/watch?v=3XbfW90grUk', '1 Mile Jog | Walk At Home Fitness Videos')
ex4 = Exercise(4, 'Do push ups', 'https://www.youtube.com/watch?v=tWjBnQX3if0','5 Minute Push Ups Workout at Home')
ex5 = Exercise(5, 'Squat', 'https://www.youtube.com/watch?v=eQ7h8I1WqEY','Weekly Workout | Squats | Squat Jump')
ex6 = Exercise(6, 'Stretch', 'https://www.youtube.com/watch?v=sTxC3J3gQEU','Total Body Stretching Warm-Up | WebMD')

db.session.add_all([ex1, ex2, ex3, ex4, ex5, ex6])
db.session.commit()

m1 = Music(1, 'Perfect Night', 'https://www.youtube.com/watch?v=hLvWy2b857I', "LE SSERAFIM (르세라핌) 'Perfect Night' OFFICIAL M/V with OVERWATCH 2")
m2 = Music(2, 'Dancing with your Ghost', 'https://www.youtube.com/watch?v=Qzc_aX8c8g4','Sasha Alex Sloan - Dancing With Your Ghost (Lyric Video)')
m3 = Music(3, 'I Love You', 'https://www.youtube.com/watch?v=sB4iOw62R3I','Billie Eilish - i love you (Lyrics)')
m4 = Music(4, 'Ceilings','https://www.youtube.com/watch?v=2bpMSpFTdzM','Lizzy McAlpine - ceilings (official video)')
m5 = Music(5, 'Starboy','https://www.youtube.com/watch?v=34Na4j8AVgA','The Weeknd - Starboy ft. Daft Punk (Official Video)')
m6 = Music(6, 'Save Your Tears','https://www.youtube.com/watch?v=XXYlFuWEuKI','The Weeknd - Save Your Tears (Official Music Video)')

db.session.add_all([m1, m2, m3, m4, m5, m6])
db.session.commit()

a1 = Advice(1, 'Smile', 'https://www.youtube.com/watch?v=pFTgWwohFz8','How to CHANGE Your SMILE Width and Shape to V SMILE')
a2 = Advice(2, 'Laugh', 'https://www.youtube.com/watch?v=xmDAdkevZOA','Daniel Piper Teaches Comedy: How To Laugh Properly')
a3 = Advice(3, 'Cry', 'https://www.youtube.com/watch?v=-122SRX3sbI' ,'The Benefits of Crying')
a4 = Advice(4, 'Sleep', 'https://www.youtube.com/watch?v=bTEZbwiOCms', '8 Benefits of Getting Quality Sleep')
a5 = Advice(5, 'Eat Healthy', 'https://www.youtube.com/watch?v=3DM3_ocFy0U', 'What Happens When You Start Eating Healthy?')
a6 = Advice(6, 'Take a walk', 'https://www.youtube.com/watch?v=hapNhZNM0jQ', 'How to walk properly: start with your feet!')

db.session.add_all([a1, a2, a3, a4, a5, a6])
db.session.commit()