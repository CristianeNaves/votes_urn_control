import sqlite3

DATABASE = './app/database.db'

class Usuario:
    def __init__(self, nome, funcao_id, empresa_id, grupo_sigla, cartorio_id, id=None):
        self.nome = nome
        self.funcao_id = funcao_id
        self.empresa_id = empresa_id
        self.grupo_sigla = grupo_sigla
        self.cartorio_id = cartorio_id
        self.id = id

def buscar_usuarios():
    usuarios = []
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("select * from usuarios")
    for usuario in cur:
        usuario = Usuario(cartorio_id=usuario[5], grupo_sigla= usuario[4], empresa_id=usuario[3], funcao_id=usuario[2], nome=usuario[1], id=usuario[0])
        usuarios.append(usuario)
    con.close()
    return usuarios

def salvar_usuario(usuario):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO usuarios (cartorio_id, grupo_sigla, empresa_id, funcao_id, nome) VALUES (?,?,?,?,?)", (usuario.cartorio_id, usuario.grupo_sigla, usuario.empresa_id, usuario.funcao_id, usuario.nome))
    con.commit()
    con.close()
