import sqlite3

DATABASE = './app/database.db'

class Engenheiro:
    def __init__(self, crea, nome, formacao, cpf=None):
        self.crea = crea
        self.nome = nome
        self.formacao = formacao
        self.cpf = cpf

def salvar_engenheiro(engenheiro):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO engenheiros (crea, nome, formacao, cpf) VALUES (?,?,?,?)", (engenheiro.crea, engenheiro.nome, engenheiro.formacao, engenheiro.cpf))
    con.commit()
    con.close()

def get_engenheiros():
    engenheiros = []
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("select * from engenheiros")
    for engenheiro in cur:
        engenheiro = Engenheiro(crea = engenheiro[1], nome = engenheiro[2], formacao = engenheiro[3], cpf = engenheiro[0])
        engenheiros.append(engenheiro)
    con.close()
    return engenheiros

def deletar_engenheiro(cpf):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("DELETE FROM engenheiros WHERE cpf = (?)", (cpf,))
    con.commit()
    con.close()

def update_engenheiro(cpf, nome, formacao, crea):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("UPDATE engenheiros SET crea = ?, nome = ?, formacao = ? WHERE cpf = ?", (crea, nome, formacao, cpf))
    con.commit()
    con.close()
