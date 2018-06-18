import sqlite3

DATABASE = './app/database.db'

class Fabricante:
    def __init__(self, local, data_fabricacao, empresa, engenheiro_cpf, id=None):
        self.local = local
        self.data_fabricacao = data_fabricacao
        self.empresa = empresa
        self.engenheiro_cpf = engenheiro_cpf
        self.id = id

def salvar_fabricante(fabricante):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO fabricantes (local, data_fabricacao, empresa, engenheiro_cpf, id) VALUES (?,?,?,?,?)", (fabricante.local, fabricante.data_fabricacao, fabricante.empresa, fabricante.engenheiro_cpf, fabricante.id))
    con.commit()
    con.close()

def get_fabricantes():
    fabricantes = []
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("select * from fabricantes")
    for fabricante in cur:
        fabricante = Fabricante(local = fabricantes[1], data_fabricacao = fabricantes[2] , empresa = fabricantes[3], engenheiro_cpf = fabricantes[4], id = fabricantes[0])
        engenheiros.append(fabricante)
    con.close()
    return fabricantes
