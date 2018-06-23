from flask import Blueprint, render_template, redirect, request
from .cartoriosDAO import salvar_cartorios, buscar_cartorios, Cartorios

cartorios_blueprint = Blueprint('cartorios', __name__, template_folder='templates')

@cartorios_blueprint.route('/cartorios')
def mostrar_cartorio():
    cartorios = buscar_cartorios()
    return render_template("mostrar_cartorio.html", cartorios = cartorios)

@cartorios_blueprint.route('/cadastrar_cartorio')
def cadastrar_cartorio():
    return render_template("cadastrar_cartorio.html")

@cartorios_blueprint.route('/criar_cartorio', methods=["POST"],)
def criar_cartorio():
    nome = request.form["nome"]
    estado_id = request.form["estado_id"]
    cartorios = Cartorios(nome=nome, estado_id=estado_id)
    salvar_cartorios(cartorios)
    return redirect('/cartorios')
