from flask import Blueprint, render_template, redirect, request
from .funcoesDAO import salvar_funcao, buscar_funcoes, deletar_funcao, atualizar_funcao, Funcao

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

@funcoes_blueprint.route('/remover_funcao', methods=["POST"])
def remover_funcao():
    id = request.form["id"]
    deletar_funcao(id)
    return redirect('/funcoes')

@funcoes_blueprint.route('/alterar_funcao', methods=["POST"])
def alterar_funcao():
    id = request.form["id"]
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    setor = request.form["setor"]
    atualizar_funcao(id, nome, descricao, setor)
    return redirect('/funcoes')

@funcoes_blueprint.route('/link_alterar_funcao', methods=["POST"])
def link_alterar_funcao():
    id = request.form["id"]
    return render_template('atualizar_funcao.html', id = id)