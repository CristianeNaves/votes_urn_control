from flask import Blueprint, render_template, redirect, request
from .fabricantesDAO import Fabricante, get_fabricantes, salvar_fabricante, deletar_fabricante, update_fabricante
from app.engenheiros.engenheirosDAO import get_engenheiros

fabricantes_blueprint = Blueprint('fabricantes', __name__, template_folder='templates')

@fabricantes_blueprint.route('/fabricantes')
def mostrar_fabricantes():
    fabricantes = get_fabricantes()
    return render_template("mostrar_fabricantes.html", fabricantes = fabricantes)

@fabricantes_blueprint.route('/cadastrar_fabricantes')
def cadastrar_fabricante():
    engenheiros = get_engenheiros();
    return render_template("cadastrar_fabricante.html", engenheiros = engenheiros)

@fabricantes_blueprint.route('/criar_fabricante', methods=["POST"])
def criar_fabricante():
    local = request.form["local"]
    data_fabricacao = request.form["data_fabricacao"]
    empresa = request.form["empresa"]
    engenheiro_cpf = int(request.form["engenheiro_cpf"])
    fab = Fabricante(local=local, data_fabricacao=data_fabricacao, empresa=empresa, engenheiro_cpf=engenheiro_cpf)
    salvar_fabricante(fab)
    return redirect('/fabricantes')

@fabricantes_blueprint.route('/remover_fabricante', methods=["POST"])
def remover_fabricante():
    id = request.form["id"]
    deletar_fabricante(id)
    return redirect('/fabricantes')

@fabricantes_blueprint.route('/alterar_fabricante', methods=["POST"])
def alterar_fabricante():
    local = request.form["local"]
    data_fabricacao = request.form["data_fabricacao"]
    empresa = request.form["empresa"]
    id = request.form["id"]
    update_fabricante(id, local, data_fabricacao, empresa)
    return redirect('/fabricantes')

@fabricantes_blueprint.route('/link_alterar_fabricante', methods=["POST"])
def link_alterar_fabricante():
    id = request.form["id"]
    return render_template('edit_fabricante.html', id = id)
