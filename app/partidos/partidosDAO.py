import sqlite3

DATABASE = './app/database.db'


class Partido:
    def __init__(self,nome, data_fundacao, lider, id=None):
        self.nome = nome
        self.data_fundacao = data_fundacao
        self.lider = lider
        self.id = id


def salvar_partido(partido):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO partidos (lider,data_fundacao, nome) VALUES (?,?,?)", (partido.lider, partido.data_fundacao, partido.nome))
    con.commit()
    con.close()

def buscar_partidos():
    partidos = []
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("select * from partidos")
    for partido in cur:
        partido = Partido(nome=partido[3], data_fundacao=partido[2], lider=partido[1], id=partido[0])
        partidos.append(partido)
    con.close()
    return partidos

def deletar_partido(partido_id):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute(
        "DELETE from partidos where id = ?",(partido_id)
    )
    con.commit()
    con.close()

def buscar_partido(partido_id):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("SELECT * FROM partidos WHERE id = ?", (partido_id,))
    partido = cur.fetchall()[0]
    partido = Partido(nome=partido[3], data_fundacao=partido[2], lider=partido[1], id=partido[0])
    con.close()
    return partido

def editar_partido(partido_id, nome, lider, data_fundacao):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("UPDATE partidos SET nome = ?, lider = ?, data_fundacao = ? WHERE id = ?", (nome, lider, data_fundacao, partido_id))
    con.commit()
    con.close()
