import sqlite3

DATABASE = './app/database.db'

class Empresa:
    def __init__(self, nome, localizacao, setor, id=None):
        self.id = id
        self.nome = nome
        self.localizacao = localizacao
        self.setor = setor

def salvar_empresa(empresa):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO empresas (id, nome, localizacao, setor) VALUES (?,?,?,?)", (empresa.id, empresa.nome, empresa.localizacao, empresa.setor))
    con.commit()
    con.close()

def buscar_empresas():
    empresas = []
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("select * from empresas")
    for empresa in cur:
        print(empresa)
        empresa = Empresa(setor=empresa[3], localizacao=empresa[2], nome=empresa[1], id=empresa[0])
        empresas.append(empresa)
    con.close()
    return empresas

def atualizar_empresa(id, nome, localizacao, setor):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("UPDATE empresas SET nome = ?, localizacao = ?, setor = ? WHERE id = ?", (nome, localizacao, setor, id))
    con.commit()
    con.close()

def deletar_empresa(id):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("DELETE FROM empresas WHERE id = (?)", (id,))
    con.commit()
    con.close()