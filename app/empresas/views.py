from flask import Blueprint, render_template, redirect, request
from .empresasDAO import salvar_empresa, buscar_empresas, Empresa

empresas_blueprint = Blueprint('empresas', __name__, template_folder='templates')

@empresas_blueprint.route('/empresas')
def mostrar_empresas():
    empresas = buscar_empresas()
    return render_template("mostrar_empresas.html", empresas = empresas)

@empresas_blueprint.route('/cadastrar_empresa')
def cadastrar_empresa():
    return render_template("cadastrar_empresa.html")

@empresas_blueprint.route('/criar_empresa', methods=["POST"])
def criar_empresa():
    nome = request.form["nome"]
    localizacao = request.form["localizacao"]
    setor = request.form["setor"]
    empresa = Empresa(nome=nome, localizacao=localizacao, setor=setor)
    salvar_empresa(empresa)
    return redirect('/empresas')