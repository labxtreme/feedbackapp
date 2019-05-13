from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SECRET_KEY']="qwerty"
application.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3306/feedback_database'
db = SQLAlchemy(application)