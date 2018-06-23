from flask import Blueprint, render_template, redirect, request
from .candidatosDAO import Candidato, buscar_candidatos, salvar_candidato
from app.partidos.partidosDAO import buscar_partidos
from app.cargos.cargosDAO import buscar_cargos

candidatos_blueprint = Blueprint('candidatos', __name__, template_folder='templates')

@candidatos_blueprint.route('/candidatos')
def mostrar_candidatos():
    candidatos = buscar_candidatos()
    return render_template("mostrar_candidatos.html", candidatos = candidatos) #colocar opcao de editar e deletar

@candidatos_blueprint.route('/editar_candidato/<int:candidato_id>', methods=["POST",])
def editar_candidato(candidato_id):
    print(candidato_id)
    return redirect("/votar")

@candidatos_blueprint.route('/deletar_candidato/<int:candidato_id>', methods=["POST",])
def deletar_candidato(candidato_id):
    print(candidato_id)
    return redirect("/votar")

@candidatos_blueprint.route('/criar_candidato', methods=["POST"])
def criar_candidato():
    print("Aqui")
    nome = request.form["nome"]
    foto = request.form["foto"]
    if(request.args.get("vice")):
        vice_id = request.form["vice"]
    else:
        vice_id = None
    cargo_id = request.form["cargo"]
    partido_id = request.form["partido"]

    print(nome)
    print(foto)
    print(vice_id)
    print(cargo_id)
    print(partido_id)

    candidato = Candidato(nome=nome,foto=foto, vice_id=vice_id, cargo_id=cargo_id, partido_id=partido_id)
    salvar_candidato(candidato)
    return render_template("index.html")

@candidatos_blueprint.route('/cadastrar_candidato')
def cadastrar_candidato():
    partidos = buscar_partidos()
    cargos = buscar_cargos()
    candidatos_vice = buscar_candidatos()
    return render_template("cadastrar_candidato.html", partidos=partidos,cargos=cargos, candidatos_vice=candidatos_vice)
