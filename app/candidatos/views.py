from flask import Blueprint, render_template, redirect, request
from .candidatosDAO import Candidato, buscar_candidatos, salvar_candidato, deletar_candidato, editar_candidato, buscar_candidato
from app.partidos.partidosDAO import buscar_partidos
from app.cargos.cargosDAO import buscar_cargos

candidatos_blueprint = Blueprint('candidatos', __name__, template_folder='templates')

@candidatos_blueprint.route('/candidatos')
def mostrar_candidatos():
    candidatos = buscar_candidatos()
    return render_template("mostrar_candidatos.html", candidatos = candidatos) #colocar opcao de editar e deletar

@candidatos_blueprint.route('/criar_edicao', methods=["POST",])
def criar_edicao():
    nome = request.form["nome"]
    candidato_id = request.form["candidato_id"]
    vice_id = request.form["vice"]
    partido_id = request.form["partido"]
    cargo_id = request.form["cargo"]
    editar_candidato(candidato_id, nome, vice_id, partido_id, cargo_id)
    return redirect('/candidatos')

@candidatos_blueprint.route('/editar_candidato/<int:candidato_id>')
def editar_candidato_view(candidato_id):
    print(candidato_id)
    candidatos_vice = buscar_candidatos()
    cargos = buscar_cargos()
    partidos = buscar_partidos()
    candidato = buscar_candidato(candidato_id)
    print(candidato)
    return render_template("editar_candidato.html", candidato = candidato, candidatos_vice=candidatos_vice, cargos=cargos, partidos=partidos)

@candidatos_blueprint.route('/deletar_candidato', methods=["POST",])
def deletar_candidato_view():
    print("deletar")
    candidato_id = request.form["candidato_id"]
    deletar_candidato(candidato_id)
    return redirect("/candidatos")

@candidatos_blueprint.route('/criar_candidato', methods=["POST"])
def criar_candidato():
    nome = request.form["nome"]
    foto = request.form["foto"]
    if(request.args.get("vice")):
        vice_id = request.form["vice"]
    else:
        vice_id = None
    cargo_id = request.form["cargo"]
    partido_id = request.form["partido"]

    candidato = Candidato(nome=nome,foto=foto, vice_id=vice_id, cargo_id=cargo_id, partido_id=partido_id)
    salvar_candidato(candidato)
    return redirect("/candidatos")

@candidatos_blueprint.route('/cadastrar_candidato')
def cadastrar_candidato():
    partidos = buscar_partidos()
    cargos = buscar_cargos()
    candidatos_vice = buscar_candidatos()
    return render_template("cadastrar_candidato.html", partidos=partidos,cargos=cargos, candidatos_vice=candidatos_vice)
