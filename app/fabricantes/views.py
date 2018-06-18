from flask import Blueprint, render_template, redirect, request
from .fabricantesDAO import Fabricante, get_fabricantes

fabricantes_blueprint = Blueprint('fabricantes', __name__, template_folder='templates')

@fabricantes_blueprint.route('/fabricantes')
def mostrar_fabricantes():
    fabricantes = get_fabricantes()
    return render_template("mostrar_fabricante.html", fabricantes = fabricantes)

@fabricantes_blueprint.route('/cadastrar_fabricantes')
def cadastrar_fabricante():
    return render_template("cadastrar_fabricante.html")

@fabricantes_blueprint.route('/criar_fabricante', methods=["POST"])
def criar_fabricante():
    local = request.form["local"]
    data_fabricacao = request.form["data_fabricacao"]
    empresa = request.form["empresa"]
    engenheiro_cpf = request.form["engenheiro_cpf"]
    id = request.form["id"]
    fab = Fabricante(local=local, data_fabricacao=data_fabricacao, empresa=empresa, engenheiro_cpf=engenheiro_cpf, id=id)
    salvar_fabricante(fab)
    return redirect('/fabricantes')
