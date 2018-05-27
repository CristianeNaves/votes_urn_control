from flask import render_template, Blueprint

users_blueprint = Blueprint('users', __name__, template_folder='templates')

@users_blueprint.route('/')
def index():
    return render_template('index.html')
