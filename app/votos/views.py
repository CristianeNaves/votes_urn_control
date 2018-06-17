from flask import render_template, Blueprint, request
import sqlite3 as sql

votos_blueprint = Blueprint('votos', __name__, template_folder='templates')

@votos_blueprint.route('/votos')
def mostrar_votos():
    print('oi')
    return render_template("index.html")
