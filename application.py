from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from application import db

application=Flask(__name__)
application.config['SECRET_KEY']="qwerty"
db.init_app(application)

login_manager=LoginManager()
login_manager.login_view='auth.login'
login_manager.init_app(application)

from application.models import employee

@login_manager.user_loader
def load_user(USER_ID):
	return employee.query.get(int(USER_ID))

from application.auth import auth as auth_bp
application.register_blueprint(auth_bp)

from application.main import main as main_bp
application.register_blueprint(main_bp)

if __name__ == '__main__':
	application.debug = True
	application.run()
