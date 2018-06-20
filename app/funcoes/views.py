from flask import Blueprint, render_template, redirect, request
from .funcoesDAO import salvar_funcao, buscar_funcoes, Funcao

funcoes_blueprint = Blueprint('funcoes', __name__, template_folder='templates')

@funcoes_blueprint.route('/funcoes')
def mostrar_funcoes():
    funcoes = buscar_funcoes()
    return render_template("mostrar_funcoes.html", funcoes = funcoes)

@funcoes_blueprint.route('/cadastrar_funcao')
def cadastrar_funcao():
    return render_template("cadastrar_funcao.html")

@funcoes_blueprint.route('/criar_funcao', methods=["POST"])
def criar_funcao():
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    setor = request.form["setor"]
    funcao = Funcao(nome=nome, descricao=descricao, setor=setor)
    salvar_funcao(funcao)
    return redirect('/funcoes')