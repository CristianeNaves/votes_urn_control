from flask import Blueprint, render_template, redirect, request
from .gruposDAO import salvar_grupo, buscar_grupos, deletar_grupo, atualizar_grupo, Grupo

grupos_blueprint = Blueprint('grupos', __name__, template_folder='templates')

@grupos_blueprint.route('/grupos')
def mostrar_grupos():
    grupos = buscar_grupos()
    return render_template("mostrar_grupos.html", grupos = grupos)

@grupos_blueprint.route('/cadastrar_grupo')
def cadastrar_grupo():
    return render_template("cadastrar_grupo.html")

@grupos_blueprint.route('/criar_grupo', methods=["POST"])
def criar_grupo():
    sigla = request.form["sigla"]
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    chefe = request.form["chefe"]
    grupo = Grupo(sigla=sigla, nome=nome, descricao=descricao, chefe=chefe)
    salvar_grupo(grupo)
    return redirect('/grupos')

@grupos_blueprint.route('/remover_grupo', methods=["POST"])
def remover_grupo():
    sigla = request.form["sigla"]
    deletar_grupo(sigla)
    return redirect('/grupos')

@grupos_blueprint.route('/alterar_grupo', methods=["POST"])
def alterar_grupo():
    sigla = request.form["sigla"]
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    chefe = request.form["chefe"]
    atualizar_grupo(sigla, nome, descricao, chefe)
    return redirect('/grupos')

@grupos_blueprint.route('/link_alterar_grupo', methods=["POST"])
def link_alterar_grupo():
    sigla = request.form["sigla"]
    return render_template('atualizar_grupo.html', sigla = sigla)