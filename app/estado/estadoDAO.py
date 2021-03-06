import sqlite3

DATABASE = './app/database.db'

class Estado:
    def __init__(self, nome, sigla, cargos_id):
        self.nome = nome
        self.sigla = sigla
        self.cargos_id = cargos_id

def salvar_estado(estado):
    con = sqlite3.connect(DATABASE)
    est = con.cursor()
    est.execute("INSERT INTO estado (id, nome, sigla, cargos_id) VALUES (?,?,?,?)", (estado.id, estado.nome, estado.sigla, estado.cargos_id))
    con.commit()
    con.close()

def buscar_estado():
    estados = []
    con = sqlite3.connect(DATABASE)
    est = con.cursor()
    est.execute("select * from estado")
    for estado in est:
        print(estado)
        estado = Estado(cargos_id=estado[3], sigla=estado[2], nome=estado[1])
        estados.append(estado)
    con.close()
    return estado