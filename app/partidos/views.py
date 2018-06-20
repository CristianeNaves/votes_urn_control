from flask import Blueprint, render_template, redirect, request
from .partidosDAO import salvar_partido, buscar_partidos, Partido, deletar_partido, buscar_partido, editar_partido

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

@partidos_blueprint.route('/deletar_partido', methods=["POST",])
def deletar_candidato_view():
    print("deletar")
    partido_id = request.form["partido_id"]
    deletar_partido(partido_id)
    return redirect("/partidos")

@partidos_blueprint.route('/criar_edicao_partido', methods=["POST",])
def criar_edicao():
    nome = request.form["nome"]
    lider = request.form["lider"]
    data_fundacao = request.form["data"]
    partido_id = request.form["partido_id"]
    editar_partido(partido_id, nome, lider, data_fundacao)
    return redirect('/partidos')

@partidos_blueprint.route('/editar_partido/<int:partido_id>')
def editar_candidato_view(partido_id):
    partido = buscar_partido(partido_id)
    return render_template("editar_partido.html", partido = partido)
