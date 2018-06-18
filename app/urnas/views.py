from flask import Blueprint, render_template, redirect, request
from .urnasDAO import salvar_urna, buscar_urnas, Urna

urnas_blueprint = Blueprint('urnas', __name__, template_folder='templates')

@urnas_blueprint.route('/urnas')
def mostrar_urnas():
    urnas = buscar_urnas()
    return render_template("mostrar_urnas.html", urnas = urnas)

@urnas_blueprint.route('/cadastrar_urnas')
def cadastrar_urna():
    return render_template("cadastrar_urna.html")

@urnas_blueprint.route('/criar_urna', methods=["POST"],)
def criar_urna():
    id = request.form["id"]
    local = request.form["local"]
    urna = Urna(id=id, local=local)
    salvar_urna(urna)
    return redirect('/urnas')
