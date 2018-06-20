from flask import render_template, Blueprint, request, redirect
import sqlite3 as sql
from datetime import datetime
from .votosDAO import salvar_voto, buscar_votos, Voto
from app.candidatos.candidatosDAO import buscar_candidato, buscar_candidatos

votos_blueprint = Blueprint('votos', __name__, template_folder='templates')

@votos_blueprint.route('/votos')
def mostrar_votos():
    votos = buscar_votos()
    return render_template("mostrar_votos.html", votos=votos, buscar_candidato=buscar_candidato)

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
    voto = Voto(regiao=regiao, urna_id=urna_id, candidato_id=candidato_id)
    salvar_voto(voto)
    return redirect('/votos')
