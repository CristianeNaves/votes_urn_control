from flask import Blueprint, render_template, redirect, request
from .engenheirosDAO import Engenheiro, get_engenheiros, salvar_engenheiro, deletar_engenheiro, update_engenheiro
engenheiros_blueprint = Blueprint('engenheiros', __name__, template_folder='templates')

@engenheiros_blueprint.route('/engenheiros')
def mostrar_engenheiros():
    engenheiros = get_engenheiros()
    return render_template("mostrar_engenheiros.html", engenheiros = engenheiros)

@engenheiros_blueprint.route('/cadastrar_engenheiro')
def cadastrar_engenheiro():
    return render_template("cadastrar_engenheiro.html")

@engenheiros_blueprint.route('/criar_engenheiro', methods=["POST"])
def criar_engenheiro():
    crea = request.form["crea"]
    nome = request.form["nome"]
    formacao = request.form["formacao"]
    cpf = request.form["cpf"]
    eng = Engenheiro(crea=crea, nome=nome, formacao=formacao, cpf=cpf)
    salvar_engenheiro(eng)
    return redirect('/engenheiros')

@engenheiros_blueprint.route('/remover_engenheiro', methods=["POST"])
def remover_engenheiro():
    cpf = request.form["cpf"]
    deletar_engenheiro(cpf)
    return redirect('/engenheiros')

@engenheiros_blueprint.route('/alterar_engenheiro', methods=["POST"])
def alterar_engenheiro():
    crea = request.form["crea"]
    nome = request.form["nome"]
    formacao = request.form["formacao"]
    cpf = request.form["cpf"]
    update_engenheiro(cpf, nome, formacao, crea)
    return redirect('/engenheiros')

@engenheiros_blueprint.route('/link_alterar_engenheiro', methods=["POST"])
def link_alterar_engenheiro():
    cpf = request.form["cpf"]
    return render_template('edit_engenheiro.html', cpf = cpf)
