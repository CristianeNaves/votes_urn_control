from flask import Blueprint, render_template, redirect, request
from .engenheirosDAO import Engenheiro, get_engenheiros

engenheiros_blueprint = Blueprint('engenheiros', __name__, template_folder='templates')

@engenheiros_blueprint.route('/engenheiros')
def mostrar_engenheiros():
    engenheiros = get_engenheiros()
    return render_template("mostrar_engenheiros.html", engenheiros = engenheiros)
