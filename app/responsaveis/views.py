from flask import Blueprint, render_template, redirect, request
from .responsaveisDAO import Responsavel, get_responsaveis, salvar_responsavel, deletar_responsavel, update_responsavel

responsaveis_blueprint = Blueprint('responsaveis', __name__, template_folder='templates')

@responsaveis_blueprint.route('/responsaveis')
def mostrar_responsaveis():
    responsaveis = get_responsaveis()
    return render_template("mostrar_responsaveis.html", responsaveis = responsaveis)

@responsaveis_blueprint.route('/cadastrar_responsavel')
def cadastrar_responsavel():
    return render_template("cadastrar_responsavel.html")

@responsaveis_blueprint.route('/criar_responsavel', methods=["POST"])
def criar_responsavel():
    cpf = request.form["cpf"]
    nome = request.form["nome"]
    data_nasc = request.form["data_nasc"]
    cartorio_id = request.form["cargos_id"]
    resp = responsavel(nome=nome, data_nasc=data_nasc, cartorio_id=cartorio_id, cpf=cpf)
    salvar_responsavel(resp)
    return redirect('/responsaveis')

@responsaveis_blueprint.route('/remover_responsavel', methods=["POST"])
def remover_responsavel():
    cpf = request.form["cpf"]
    deletar_responsavel(cpf)
    return redirect('/responsaveis')

@responsaveis_blueprint.route('/alterar_responsavel', methods=["POST"])
def alterar_responsavel():
    nome = request.form["nome"]
    data_nasc = request.form["data_nasc"]
    cpf = request.form["cpf"]
    update_engenheiro(cpf, nome, data_nasc)
    return redirect('/responsaveis')

@responsaveis_blueprint.route('/link_alterar_responsavel', methods=["POST"])
def link_alterar_responsavel():
    cpf = request.form["cpf"]
    return render_template('edit_responsavel.html', cpf = cpf)
