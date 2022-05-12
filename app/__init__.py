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
    app = Flask(__name__)

    from .auth import auth as authentication_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(main_blueprint)
    app.config['SECRET_KEY']='1234'
    app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:lee123@localhost/pitch'


    login_manager.init_app(app)
    db.init_app(app)
    bootstap.init_app(app)
    


    return app