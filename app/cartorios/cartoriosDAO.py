import sqlite3

DATABASE = './app/database.db'

class Cartorios:
    def __init__(self, nome, estado_id):
        self.id = id
        self.nome = nome
        self.estado_id = estado_id

def salvar_cartorios(cartorios):
    con = sqlite3.connect(DATABASE)
    cart = con.cursor()
    cart.execute("INSERT INTO cartorios (id, nome, estado_id) VALUES (?,?,?)", (cartorios.id, cartorios.nome, cartorios.estado_id))
    con.commit()
    con.close()

def buscar_cartorios():
    cartorios = []
    con = sqlite3.connect(DATABASE)
    cart = con.cursor()
    cart.execute("select * from cartorios")
    for cartorios in cart:
        print(cartorios)
        cartorios = Cartorios(estado_id=cartorios[2], nome=cartorios[1])
        cartorios.append(cartorios)
    con.close()
    return cartorios

	