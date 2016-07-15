from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

#setting the configuration of the application from a settings file
app.config.from_object('settings')
db = SQLAlchemy(app)


#from here i created the home directory to create the views.py

#this will import the views.py from the home folder
from blog import views
from author import views

#after the above i created the settings file on the floor of the flask_blog