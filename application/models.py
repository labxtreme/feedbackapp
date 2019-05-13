from flask_login import UserMixin
from application import db

class employee(db.Model, UserMixin):
	__tablename__ = 'employee'
	id = db.Column(db.Integer, primary_key=True)
	Ename = db.Column(db.String(1000))
	Eid = db.Column(db.Integer, unique=True)
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	role = db.Column(db.String(10), default="RECRUITER" )

class user_req(db.Model, UserMixin):
    __tablename__ = 'user_req'
    id = db.Column(db.Integer, primary_key=True)
    Ename = db.Column(db.String(1000))
    Eid = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(10), default="RECRUITER" )

class feedback_store(db.Model, UserMixin):
    __tablename__='feedback_store'
    id = db.Column(db.Integer, primary_key=True)
    Eid = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(100), unique=True)
    feedback_text=db.Column(db.String(1000))

class good_feedback(db.Model, UserMixin):
    __tablename__='good_feedback'
    id = db.Column(db.Integer, primary_key=True)
    feedback_text=db.Column(db.String(1000))

class bad_feedback(db.Model, UserMixin):
    __tablename__='bad_feedback'
    id = db.Column(db.Integer, primary_key=True)
    feedback_text=db.Column(db.String(1000))