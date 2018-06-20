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
    cur.execute("INSERT INTO fabricantes (local, data_fabricacao, empresa, engenheiro_cpf) VALUES (?,?,?,?)", (fabricante.local, fabricante.data_fabricacao, fabricante.empresa, fabricante.engenheiro_cpf))
    con.commit()
    con.close()

def get_fabricantes():
    fabricantes = []
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("select * from fabricantes")
    for fabricante in cur:
        fabricante = Fabricante(local = fabricante[1], data_fabricacao = fabricante[2] , empresa = fabricante[3], engenheiro_cpf = fabricante[4], id=fabricante[0])
        fabricantes.append(fabricante)
    con.close()
    return fabricantes

def deletar_fabricante(id):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    id = str(id)
    cur.execute("DELETE FROM fabricantes WHERE id = (?)", (id,))
    con.commit()
    con.close()
