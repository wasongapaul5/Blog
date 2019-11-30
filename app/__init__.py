from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_wtf.csrf import CSRFProtect

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.config['SECRET_KEY']= 'VGACDGWAGHV'

    db.init_app =(app)
    login_manager.init_app(app)
    bootstrap.init_app = Bootstrap(app)
    mail.init_app(app)
    csrf.init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
