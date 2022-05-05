from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Role
# Creating app instance
app = create_app('development')
manager = Manager(app)
manager.add_command('server',Server)
@manager.shell # helps us to create the shell context
def make_shell_context():# to allow us pass in some properties into our shell.
    return dict(app = app,db = db,User = User,Role = Role)
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
if (__name__) == '__main__':
    manager.run()
    # flask_script shell to allow us create a python shell inside our application
    # command to open the python shell in terminal is python3.9 manage.py shell
    #to confirm that our items have been passed in we type them in the shell to see. eg db,User,app.
    # command to create tables and columns in our database is db.create_all() but before creating make sure to enter the password set in the terminal
    #CRUD using sqlalchemy(Create,Read,Update,Delete)