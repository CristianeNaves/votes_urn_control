from flask import Blueprint, render_template, redirect, request
from .engenheirosDAO import Engenheiro, get_engenheiros, salvar_engenheiro

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
