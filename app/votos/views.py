from flask import render_template, Blueprint, request, redirect
import sqlite3 as sql
from datetime import datetime
from .votosDAO import salvar_voto

votos_blueprint = Blueprint('votos', __name__, template_folder='templates')

class Voto:
    def __init__(self, regiao, id_urna, id_candidato, horario=None):
        self.horario = datetime.now()
        self.regiao = regiao
        self.id_urna = id_urna
        self.id_candidato = id_candidato

@votos_blueprint.route('/votos')
def mostrar_votos():
    return render_template("index.html")

@votos_blueprint.route('/votar')
def votar():
    candidatos = buscar_candidatos()
    print(candidatos)
    return render_template("registrar_voto.html", candidatos= candidatos)

@votos_blueprint.route('/criar_voto', methods=['POST',])
def criar_voto():
    candidato_id = request.form["id_candidato"]
    regiao = request.form["regiao"]
    urna_id = 1
    voto = Voto(regiao=regiao, id_urna=urna_id, id_candidato=candidato_id)
    salvar_voto(voto)
    return redirect('/votos')

#metodo DAO
def buscar_candidatos():
    #busco todos os candidatos e retorno as_dict
    return [{'nome': 'candidato1', 'id': 1}, {'nome': 'candidato2', 'id': 2}]
