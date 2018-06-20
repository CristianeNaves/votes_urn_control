from flask import Blueprint, render_template, redirect, request
from .usuariosDAO import Usuario, buscar_usuarios, salvar_usuario
from app.funcoes.funcoesDAO import buscar_funcoes
from app.empresas.empresasDAO import buscar_empresas
from app.grupos.gruposDAO import buscar_grupos
# from app.cartorios.cartoriosDAO import buscar_cartorios

usuarios_blueprint = Blueprint('usuarios', __name__, template_folder='templates')

@usuarios_blueprint.route('/usuarios')
def mostrar_usuarios():
    usuarios = buscar_usuarios()
    return render_template("mostrar_usuarios.html", usuarios = usuarios)

@usuarios_blueprint.route('/editar_usuario/<int:usuario_id>', methods=["POST",])
def editar_usuario(usuario_id):
    print(usuario_id)
    return redirect("/usuarios")

# @usuarios_blueprint.route('/deletar_usuario/<int:usuario_id>', methods=["POST",])
# def deletar_usuario(usuario_id):
#     print(usuario_id)
#     return redirect("/usuarios")

@usuarios_blueprint.route('/criar_usuario', methods=["POST"])
def criar_usuario():
    # print("Aqui")
    nome = request.form["nome"]
    funcao_id = request.form["funcao"]
    empresa_id = request.form["empresa"]
    grupo_sigla = request.form["grupo"]
    # cartorio_id = request.form["cartorio"]

    print(nome)
    print(funcao_id)
    print(empresa_id)
    print(grupo_sigla)
    # print(cartorio_id)

    usuario = Usuario(nome=nome, funcao_id=funcao_id, empresa_id=empresa_id, grupo_sigla=grupo_sigla)#, cartorio_id=cartorio_id)
    salvar_usuario(usuario)
    return render_template("usuarios.html")

@usuarios_blueprint.route('/cadastrar_usuario')
def cadastrar_usuario():
    funcoes = buscar_funcoes()
    empresas = buscar_empresas()
    grupos = buscar_grupos()
    # cartorios = buscar_cartorios()
    return render_template("cadastrar_usuario.html", funcoes=funcoes, empresas=empresas, grupos=grupos)#, cartorios=cartorios)
