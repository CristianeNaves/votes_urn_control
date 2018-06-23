import sqlite3

DATABASE = './app/database.db'

class Cargo:
    def __init__(self, nome, descricao=None, poder=None, local_trabalho=None, id=None):
        self.nome = nome
        self.id = id
        self.descricao = descricao
        self.poder = poder
        self.local_trabalho = local_trabalho

def salvar_cargo(cargo):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO cargos (nome, descricao, poder, local_trabalho) VALUES (?,?,?,?)", (cargo.nome, cargo.descricao, cargo.poder, cargo.local_trabalho))
    con.commit()
    con.close()

def buscar_cargos():
    cargos = []
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("select * from cargos")
    for cargo in cur:
        print(cargo)
        cargo = Cargo(local_trabalho=cargo[4], poder=cargo[3], descricao=cargo[2], nome=cargo[1], id=cargo[0])
        cargos.append(cargo)
    con.close()
    return cargos

def deletar_cargo(cargo_id):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute(
        "DELETE from cargos where id = ?",(cargo_id)
    )
    con.commit()
    con.close()

def buscar_cargo(cargo_id):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("SELECT * FROM cargos WHERE id = ?", (cargo_id,))
    cargo = cur.fetchall()[0]
    cargo = Cargo(local_trabalho=cargo[4],poder=cargo[3],descricao=cargo[2],nome=cargo[1],id=cargo[0])
    con.close()
    return cargo

def editar_cargo(cargo_id, nome, descricao, poder, local_trabalho):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("UPDATE cargos SET nome = ?, descricao = ?, poder = ?, local_trabalho = ? WHERE id = ?", (nome, descricao, poder, local_trabalho,cargo_id))
    con.commit()
    con.close()
