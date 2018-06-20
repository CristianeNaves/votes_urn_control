import sqlite3

DATABASE = './app/database.db'

class Grupo:
    def __init__(self, sigla, nome, descricao, chefe):
        self.sigla = sigla
        self.nome = nome
        self.descricao = descricao
        self.chefe = chefe

def salvar_grupo(grupo):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO grupos (sigla, nome, descricao, chefe) VALUES (?,?,?,?)", (grupo.sigla, grupo.nome, grupo.descricao, grupo.chefe))
    con.commit()
    con.close()

def buscar_grupos():
    grupos = []
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("select * from grupos")
    for grupo in cur:
        print(grupo)
        grupo = Grupo(chefe=grupo[3], descricao=grupo[2], nome=grupo[1], sigla=grupo[0])
        grupos.append(grupo)
    con.close()
    return grupos

def atualizar_grupo(sigla, nome, descricao, chefe):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("UPDATE grupos SET nome = ?, descricao = ?, chefe = ? WHERE sigla = ?", (nome, descricao, chefe, sigla))
    con.commit()
    con.close()

def deletar_grupo(sigla):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("DELETE FROM grupos WHERE sigla = (?)", (sigla,))
    con.commit()
    con.close()