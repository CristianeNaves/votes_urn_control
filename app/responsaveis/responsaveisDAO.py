import sqlite3

DATABASE = './app/database.db'

class Responsavel:
    def __init__(self, nome, data_nasc, cartorio_id, cpf=None):
        self.nome = nome
        self.data_nasc = data_nasc
        self.cartorio_id = cartorio_id
        self.cpf = cpf

def salvar_responsavel(responsavel):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO responsaveis (nome, data_nasc, cartorio_id, cpf) VALUES (?,?,?,?)", (responsavel.nome, responsavel.data_nasc, responsavel.cartorio_id, responsavel.cpf))
    con.commit()
    con.close()

def get_responsaveis():
    responsaveis = []
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("select * from responsaveis")
    for responsavel in cur:
        responsavel = Responsavel(nome = responsavel[1], data_nasc = responsavel[2], cartorio_id = responsavel[3], cpf = responsavel[0])
        responsavels.append(responsavel)
    con.close()
    return responsaveis

def deletar_responsavel(cpf):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("DELETE FROM responsaveis WHERE cpf = (?)", (cpf,))
    con.commit()
    con.close()
