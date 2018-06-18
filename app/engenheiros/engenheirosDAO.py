import sqlite3

DATABASE = './app/database.db'

class Engenheiro:
    def __init__(self, crea, nome, formacao, cpf=None):
        self.crea = crea
        self.nome = nome
        self.formacao = formacao
        self.cpf = cpf

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
