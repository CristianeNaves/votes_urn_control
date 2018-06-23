from flask import Blueprint, render_template, redirect, request
from .cargosDAO import salvar_cargo, buscar_cargos, Cargo, deletar_cargo, buscar_cargo, editar_cargo

cargos_blueprint = Blueprint('cargos', __name__, template_folder='templates')

@cargos_blueprint.route('/cargos')
def mostrar_cargos():
    cargos = buscar_cargos()
    return render_template("mostrar_cargos.html", cargos = cargos)

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

@cargos_blueprint.route('/deletar_cargo', methods=["POST",])
def deletar_cargo_view():
    print("deletar")
    cargo_id = request.form["cargo_id"]
    deletar_cargo(cargo_id)
    return redirect("/cargos")

@cargos_blueprint.route('/criar_edicao_cargo', methods=["POST",])
def criar_edicao():
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    poder = request.form["poder"]
    local_trabalho = request.form["local_trabalho"]
    cargo_id = request.form["cargo_id"]
    editar_cargo(cargo_id, nome, descricao, poder, local_trabalho)
    return redirect('/cargos')

@cargos_blueprint.route('/editar_cargo/<int:cargo_id>')
def editar_cargo_view(cargo_id):
    cargo = buscar_cargo(cargo_id)
    print(cargo)
    return render_template("editar_cargo.html", cargo = cargo)
