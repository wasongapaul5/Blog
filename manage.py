from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from flask import Flask, render_template
import sys
import logging


from app import create_app, db
from app.models import User,Post
app = Flask(__name__)
app = create_app('production')

manager = Manager(app)
manager.add_command('server', Server(use_debugger=True))

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User ,Post = Post)

if __name__ == '__main__':
    manager.run()
    
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

 