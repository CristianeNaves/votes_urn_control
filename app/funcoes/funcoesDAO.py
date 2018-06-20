import sqlite3

DATABASE = './app/database.db'

class Funcao:
    def __init__(self, nome, descricao, setor, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.setor = setor

def salvar_funcao(funcao):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO funcoes (id, nome, descricao, setor) VALUES (?,?,?,?)", (funcao.id, funcao.nome, funcao.descricao, funcao.setor))
    con.commit()
    con.close()

def buscar_funcoes():
    funcoes = []
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("select * from funcoes")
    for funcao in cur:
        print(funcao)
        funcao = Funcao(setor=funcao[3], descricao=funcao[2], nome=funcao[1], id=funcao[0])
        funcoes.append(funcao)
    con.close()
    return funcoes

def atualizar_funcao(id, nome, descricao, setor):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("UPDATE funcoes SET nome = ?, descricao = ?, setor = ? WHERE id = ?", (nome, descricao, setor, id))
    con.commit()
    con.close()

def deletar_funcao(id):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("DELETE FROM funcoes WHERE id = (?)", (id,))
    con.commit()
    con.close()