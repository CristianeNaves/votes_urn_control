#setting up the Flask application and registering the different Blueprints
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
#app.config.from_pyfile('flask.cfg')

from app.users.views import users_blueprint

app.register_blueprint(users_blueprint)
