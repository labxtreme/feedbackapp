from flask import Blueprint, render_template, redirect, url_for, flash, request
from hashlib import sha256
from application.models import user_req, employee
from application import db
from flask_login import login_user, logout_user, login_required

def hash_password(password):
    return sha256(password.encode()).hexdigest()

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
		return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
	Eid=request.form.get('EID')
	password=request.form.get('password')
	remember= True if request.form.get('Remember') else False

	emp = employee.query.filter_by(Eid=Eid).first()

	if emp and (hash_password(password)==emp.password):
		login_user(emp)
	
		return redirect(url_for('main.profile'))
	
	flash('Please check your login details and try again')
	
	return redirect(url_for('auth.login'))



@auth.route('/signup')
def signup():
	return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
	name =request.form.get('Ename')
	ID =request.form.get('EID')
	email =request.form.get('emailsignup')
	password =request.form.get('passwordsignup')

	user = employee.query.filter_by(email=email).first()

	if user:
		flash('Email address already exists.')
		return redirect(url_for('auth.signup'))

	new_user=user_req(Ename=name, Eid=ID, email=email, password=hash_password(password))

	db.session.add(new_user)
	db.session.commit()

	return redirect(url_for('auth.login'))



@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('main.index'))
