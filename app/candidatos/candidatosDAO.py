import sqlite3

DATABASE = './app/database.db'

class Candidato:
    def __init__(self, nome, cargo_id, partido_id, id=None, vice_id=None, foto=None):
        self.nome = nome
        self.vice_id = vice_id
        self.cargo_id = cargo_id
        self.partido_id = partido_id
        self.foto = foto

def buscar_candidatos():
    candidatos = []
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("select * from candidatos")
    for candidato in cur:
        candidato = Candidato(partido_id=candidato[5] ,cargo_id= candidato[4],vice_id=candidato[3], foto=candidato[2], nome=candidato[1], id=candidato[0])
        candidatos.append(candidato)
    con.close()
    return candidatos

def salvar_candidato(candidato):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO candidatos (nome,foto, vice_id, cargo_id, partido_id) VALUES (?,?,?,?,?)", (candidato.nome, candidato.foto, candidato.vice_id, candidato.cargo_id, candidato.partido_id))
    con.commit()
    con.close()
