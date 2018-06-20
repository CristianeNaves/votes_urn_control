from flask import Blueprint, render_template, redirect, request
from .logsDAO import salvar_logs, buscar_logs

logs_blueprint = Blueprint('logs', __name__, template_folder='templates')

@logs_blueprint.route('/logs')
def mostrar_log():
    logs = buscar_logs()
    return render_template("mostrar_logs.html", logs = logs)

@logs_blueprint.route('/cadastrar_logs')
def cadastrar_logs():
    return render_template("cadastrar_logs.html")

@logs_blueprint.route('/criar_logs', methods=["POST"],)
def criar_logs():
    data_ = request.form["data_"]
    tipo_requisicao = request.form["tipo_requisicao"]
	parametros = request.form["parametros"]
	resultado = request.form["resultado"]
    logs = Logs(data_=data_, tipo_requisicao=tipo_requisicao, parametros=parametros, resultado=resultado)
    salvar_logs(logs)
    return redirect('/logs')
