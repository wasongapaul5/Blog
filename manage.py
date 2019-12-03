from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from app import create_app, db
from app.models import User

app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server(use_debugger=True))

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.shell
def add_shell_context():
    return {'db': db, 'User': User}


if __name__ == '__main__':
    manager.run()
 