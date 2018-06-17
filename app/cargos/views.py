from flask import Blueprint, render_template, redirect, request
from .cargosDAO import salvar_cargo, buscar_cargos, Cargo

cargos_blueprint = Blueprint('cargos', __name__, template_folder='templates')

@cargos_blueprint.route('/cargos')
def mostrar_cargos():
    cargos = buscar_cargos()
    return render_template("mostrar_cargos.html", cargos = cargos)
    pass

@cargos_blueprint.route('/cadastrar_cargo')
def cadastrar_cargo():
    return render_template("cadastrar_cargo.html")

@cargos_blueprint.route('/criar_cargo', methods=["POST"],)
def criar_cargo():
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    poder = request.form["poder"]
    local_trabalho = request.form["local_trabalho"]
    cargo = Cargo(nome=nome, descricao=descricao, poder=poder, local_trabalho=local_trabalho)
    salvar_cargo(cargo)
    return redirect('/cargos')
