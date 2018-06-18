import sqlite3

DATABASE = './app/database.db'

class Urna:
    def __init__(self, local, id=None):
        self.local = local
        self.id = id

def salvar_urna(urna):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO urnas (local, id) VALUES (?,?)", (urna.local, urna.id))
    con.commit()
    con.close()

def buscar_urnas():
    urnas = []
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("select * from urnas")
    for urna in cur:
        urna = Urna(id=urna[0], local=urna[1])
        urnas.append(urna)
    con.close()
    return urnas
