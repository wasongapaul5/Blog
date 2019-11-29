from app import creat_app
from app.models import User
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager,Server

app = create_app()

manager = Manager(app)
manager.add_command('server', Server(use_debugger=True))

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)