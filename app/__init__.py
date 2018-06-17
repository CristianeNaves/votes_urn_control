#setting up the Flask application and registering the different Blueprints
from flask import Flask, g
import sqlite3


app = Flask(__name__, instance_relative_config=True)

from app.users.views import users_blueprint
from app.votos.views import votos_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(votos_blueprint)

DATABASE = './app/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
