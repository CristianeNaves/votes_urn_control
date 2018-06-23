#setting up the Flask application and registering the different Blueprints
from flask import Flask, g
import sqlite3


app = Flask(__name__, instance_relative_config=True)

from app.users.views import users_blueprint
from app.votos.views import votos_blueprint
from app.partidos.views import partidos_blueprint
from app.cargos.views import cargos_blueprint
from app.engenheiros.views import engenheiros_blueprint
from app.fabricantes.views import fabricantes_blueprint
from app.urnas.views import urnas_blueprint
from app.candidatos.views import candidatos_blueprint
from app.usuarios.views import usuarios_blueprint
from app.empresas.views import empresas_blueprint
from app.funcoes.views import funcoes_blueprint
from app.grupos.views import grupos_blueprint
from app.responsaveis.views import responsaveis_blueprint
from app.cartorios.views import cartorios_blueprint
from app.estado.views import estados_blueprint


app.register_blueprint(users_blueprint)
app.register_blueprint(votos_blueprint)
app.register_blueprint(partidos_blueprint)
app.register_blueprint(cargos_blueprint)
app.register_blueprint(engenheiros_blueprint)
app.register_blueprint(fabricantes_blueprint)
app.register_blueprint(urnas_blueprint)
app.register_blueprint(candidatos_blueprint)
app.register_blueprint(empresas_blueprint)
app.register_blueprint(funcoes_blueprint)
app.register_blueprint(grupos_blueprint)
app.register_blueprint(usuarios_blueprint)
app.register_blueprint(responsaveis_blueprint)
app.register_blueprint(cartorios_blueprint)
app.register_blueprint(estados_blueprint)

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
