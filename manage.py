from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager,Server
from app.models import User

from app import create_app

app = create_app()

manager = Manager(app)
manager.add_command('server', Server(use_debugger=True))

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()