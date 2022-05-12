from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bootstap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'



def create_app():
    app = Flask(__name__, debug=True)

    from .auth import auth as authentication_blueprint
    login_manager.init_app(app)
    db.init_app(app)
    bootstap.init_app(app)
    


    return app