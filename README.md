# sofe3700-final-project

Data Management Systems

Final Project

### Created By:
- Emily Lai
- Natasha Naorem
- Alina Mathew
- Jonathan Hua

### Installation and Execution Instructions

1. In a Command Prompt, navigate to the project folder (virtual environment ‘db37’) and run

```bash
pip install –r requirements.txt
```

```bash
set FLASK_APP = app.py
```

2. To reset database data to default, 

- a. Delete ‘migrations’ folder and ‘data.sqlite’ file

- b. In the VSCode Terminal Command Prompt set to the proper virtual environment:

```bash
flask db init
```
```bash
python insert.py
```
```bash
flask db migrate –m “INSERT OPTIONAL COMMENT HERE”
```
```bash
flask db upgrade
```

3. To run the app, in the VSCode Terminal Command prompt type

```bash
python app2.py
```
