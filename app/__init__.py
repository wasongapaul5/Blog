from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from config import Config

app = Flask(__name__)
db = SQLAlchemy(app)
csrf=CSRFProtect()
login_manager = LoginManager()
login_manager.init_app(app)

csrf.init_app(app)
bootstrap = Bootstrap(app)
mail = Mail(app)
login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'
login_manager.login_message_category = 'info'


def create_app(config_name):
    app.config.from_object(Config)
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    return app
