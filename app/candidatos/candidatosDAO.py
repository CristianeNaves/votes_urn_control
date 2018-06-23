import sqlite3

DATABASE = './app/database.db'

class Candidato:
    def __init__(self, nome, cargo_id, partido_id, id=None, vice_id=None, foto=None):
        self.nome = nome
        self.vice_id = vice_id
        self.cargo_id = cargo_id
        self.partido_id = partido_id
        self.foto = foto
        self.id = id

def buscar_candidatos():
    candidatos = []
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("SELECT * from candidatos")
    for candidato in cur:
        print(candidato)
        candidato = Candidato(partido_id=candidato[5] ,cargo_id= candidato[4],vice_id=candidato[3], foto=candidato[2], nome=candidato[1], id=candidato[0])
        candidatos.append(candidato)
    con.close()
    return candidatos

def buscar_candidato(candidato_id):
    print(candidato_id)
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("SELECT * FROM candidatos WHERE id = ?", (candidato_id,))
    candidato = cur.fetchall()[0]
    print(candidato)
    candidato = Candidato(partido_id=candidato[5] ,cargo_id= candidato[4],vice_id=candidato[3], foto=candidato[2], nome=candidato[1], id=candidato[0])
    con.close()
    return candidato

def salvar_candidato(candidato):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO candidatos (nome,foto, vice_id, cargo_id, partido_id) VALUES (?,?,?,?,?)", (candidato.nome, candidato.foto, candidato.vice_id, candidato.cargo_id, candidato.partido_id))
    con.commit()
    con.close()

def editar_candidato(candidato_id, nome, vice_id, partido_id, cargo_id):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("UPDATE candidatos SET nome = ?, vice_id = ?, cargo_id = ?, partido_id = ? WHERE id = ?", (nome, vice_id, cargo_id, partido_id,candidato_id))
    con.commit()
    con.close()

def deletar_candidato(candidato_id):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute(
        "DELETE from candidatos where id = ?",(candidato_id)
    )
    con.commit()
    con.close()
