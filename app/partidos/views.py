from flask import Blueprint, render_template, redirect, request
from .partidosDAO import salvar_partido, buscar_partidos, Partido

partidos_blueprint = Blueprint('partidos', __name__, template_folder='templates')

@partidos_blueprint.route('/partidos')
def mostrar_partidos():
    partidos = buscar_partidos()
    return render_template("mostrar_partidos.html", partidos = partidos)

@partidos_blueprint.route('/cadastrar_partido')
def cadastrar_partido():
    return render_template("cadastrar_partido.html")

@partidos_blueprint.route('/criar_partido', methods=["POST"],)
def criar_partido():
    nome = request.form["nome"]
    data_fundacao = request.form["data_fundacao"]
    lider = request.form["lider"]
    partido = Partido(nome=nome, data_fundacao=data_fundacao,lider=lider)
    salvar_partido(partido)
    return redirect('/partidos')
