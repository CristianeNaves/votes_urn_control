import sqlite3
from datetime import datetime

DATABASE = './app/database.db'

class Voto:
    def __init__(self, urna_id, candidato_id, id=None, regiao=None, horario=None):
        self.horario = datetime.now()
        self.regiao = regiao
        self.urna_id = urna_id
        self.candidato_id = candidato_id
        self.id = id

def salvar_voto(voto):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO votos (horario,regiao, urna_id, candidato_id) VALUES (?,?,?,?)", (voto.horario, voto.regiao, voto.urna_id, voto.candidato_id))
    con.commit()
    con.close()

def buscar_votos():
    votos = []
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("SELECT * from votos")
    for voto in cur:
        voto = Voto(candidato_id=voto[4],urna_id=voto[3],regiao=voto[2],horario=voto[1],id=voto[0])
        votos.append(voto)
    con.close()
    return votos
