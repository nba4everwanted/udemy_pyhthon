import os 

SECRET_KEY = 'you-will-never-guess'
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = 'root'
BLOG_DATABASE_NAME = 'blog'
DB_HOST = os.getenv('IP','127.0.0.1')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

#from i then created manage.py on the floor of the flask_blog