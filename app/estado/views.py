from flask import Blueprint, render_template, redirect, request
from .estadoDAO import salvar_estado, buscar_estado

estado_blueprint = Blueprint('estado', __name__, template_folder='templates')

@estado_blueprint.route('/estado')
def mostrar_estado():
    estado = buscar_estado()
    return render_template("mostrar_estado.html", estado = estado)

@estado_blueprint.route('/cadastrar_estado')
def cadastrar_estado():
    return render_template("cadastrar_estado.html")

@estado_blueprint.route('/criar_estado', methods=["POST"],)
def criar_estado():
    nome = request.form["nome"]
    sigla = request.form["sigla"]
	cargos_id = request.form["cargos_id"]
	cartorios_id = request.form["cartorios_id"]
    estado = Estado(nome=nome, sigla=sigla, cargos_id=cargos_id, cartorios_id=cartorios_id)
    salvar_estado(estado)
    return redirect('/estado')
