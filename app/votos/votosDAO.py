import sqlite3

DATABASE = './app/database.db'

def salvar_voto(voto):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO votos (horario,regiao, urna_id, candidato_id) VALUES (?,?,?,?)", (voto.horario, voto.regiao, voto.id_urna, voto.id_candidato))
    con.commit()
    con.close()
