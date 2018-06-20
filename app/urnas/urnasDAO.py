import sqlite3

DATABASE = './app/database.db'

class Urna:
    def __init__(self, local, fabricante_id, id=None):
        self.local = local
        self.fabricante_id = fabricante_id
        self.id = id

def salvar_urna(urna):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO urnas (local, fabricante_id) VALUES (?,?)", (urna.local, urna.fabricante_id))
    con.commit()
    con.close()

def buscar_urnas():
    urnas = []
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("select * from urnas")
    for urna in cur:
        urna = Urna(id=urna[0], local=urna[1], fabricante_id = urna[2])
        urnas.append(urna)
    con.close()
    return urnas

def deletar_urna(id):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    id = str(id)
    cur.execute("DELETE FROM urnas WHERE id = (?)", (id,))
    con.commit()
    con.close()
