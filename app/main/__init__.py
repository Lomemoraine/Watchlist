from flask import Flask

# from config import DevConfig # import the DevConfig class from the config file in app folder so that you can use it
# from flask_bootstrap import Bootstrap

# # Initializing application
app = Flask(__name__,instance_relative_config = True)
# # Initializing Flask Extensions
# bootstrap = Bootstrap(app)

# # Setting up configuration
# app.config.from_object(DevConfig) #set up configuration and pass in the subclass(DevConfig)
# app.config.from_pyfile('config.py')
# from app.main import views
# from app.main import error
from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,errors
def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
def create_app(config_name):
    #....
    # Registering the blueprint
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from ..request import configure_request
    configure_request(app)

    return app