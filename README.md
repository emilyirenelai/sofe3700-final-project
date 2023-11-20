# sofe3700-final-project

Data Management Systems

Final Project

### Created By:
- Emily Lai
- Natasha Naorem
- Alina Mathew
- Jonathan Hua

### Installation and Execution Instructions
Note: Please use Python 3.7.0 or lower.

1. In a Command Prompt, navigate to the project folder (virtual environment ‘db37’) and run

pip install –r requirements.txt
set FLASK_APP = app.py

2. To reset database data to default, 
a. Delete ‘migrations’ folder and ‘data.sqlite’ file
b. In the VSCode Terminal Command Prompt set to the proper virtual environment:

flask db init
python insert.py
flask db migrate –m “INSERT OPTIONAL COMMENT HERE”
flask db upgrade

3. To run the app, in the VSCode Terminal Command prompt type

python app.py

TODO:
-Fix “TODO”s in the Python code, including Cohere functionality
-Get the buttons in the Add and Delete pages to navigate to the List page
-Incorporate an Admin page to search users by letter in name, etc.
-Get Delete and Add functions to work
-Make UI nice

