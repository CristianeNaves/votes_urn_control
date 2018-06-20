from flask import render_template, Blueprint, request, redirect
import sqlite3 as sql
from datetime import datetime
from .votosDAO import salvar_voto, buscar_votos, Voto, deletar_voto, buscar_regiao, editar_voto
from app.candidatos.candidatosDAO import buscar_candidato, buscar_candidatos
from app.urnas.urnasDAO import buscar_urnas

votos_blueprint = Blueprint('votos', __name__, template_folder='templates')

@votos_blueprint.route('/votos')
def mostrar_votos():
    votos = buscar_votos()
    return render_template("mostrar_votos.html", votos=votos, buscar_candidato=buscar_candidato)

@votos_blueprint.route('/votar')
def votar():
    candidatos = buscar_candidatos()
    urnas = buscar_urnas()
    print(candidatos)
    return render_template("registrar_voto.html", candidatos= candidatos, urnas=urnas)

@votos_blueprint.route('/criar_voto', methods=['POST',])
def criar_voto():
    candidato_id = request.form["id_candidato"]
    regiao = request.form["regiao"]
    urna_id = request.form["urna_id"]
    voto = Voto(regiao=regiao, urna_id=urna_id, candidato_id=candidato_id)
    salvar_voto(voto)
    return redirect('/votos')

@votos_blueprint.route('/deletar_voto', methods=["POST",])
def deletar_voto_view():
    print("deletar")
    voto_id = request.form["voto_id"]
    deletar_voto(voto_id)
    return redirect("/votos")

@votos_blueprint.route('/criar_edicao_voto', methods=["POST",])
def criar_edicao():
    regiao = request.form["regiao"]
    voto_id = request.form["voto_id"]
    editar_voto(voto_id, regiao)
    return redirect('/votos')

@votos_blueprint.route('/editar_voto/<int:voto_id>')
def editar_voto_view(voto_id):
    regiao = buscar_regiao(voto_id)
    return render_template("editar_voto.html", regiao=regiao, voto_id = voto_id)
