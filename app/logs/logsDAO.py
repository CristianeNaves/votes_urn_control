import sqlite3

DATABASE = './app/database.db'

class Logs:
    def __init__(self, data_, tipo_requisicao, parametros, resultado):
        self.data_ = data_
        self.tipo_requisicao = tipo_requisicao
        self.parametros = parametros
        self.resultado = resultado

def salvar_logs(logs):
    con = sqlite3.connect(DATABASE)
    log_ = con.cursor()
    log_.execute("INSERT INTO logs (id, data_, tipo_requisicao, parametros, resultado) VALUES (?,?,?,?,?)", (logs.id, logs.data_, logs.tipo_requisicao, logs.parametros. logs.resultado))
    con.commit()
    con.close()

def buscar_logs():
    logs = []
    con = sqlite3.connect(DATABASE)
    log_ = con.cursor()
    log_.execute("select * from logss")
    for logs in log_:
        print(logs)
        logs = logs(resultado=logs[4],parametros=logs[3], tipo_requisicao=logs[2], data_=logs[1], id=logs[0])
        logs.append(logs)
    con.close()
    return logs
