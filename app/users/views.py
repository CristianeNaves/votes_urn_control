from flask import render_template, Blueprint, request
import sqlite3 as sql

users_blueprint = Blueprint('users', __name__, template_folder='templates')

@users_blueprint.route('/')
def index():
    con = sql.connect("app/database.db")
    cur = con.cursor()
    cur.execute("select * from users")
    users = cur.fetchall()
    con.close()
    print(users)

    return render_template('index.html')

@users_blueprint.route('/register_user')
def register_user():
    return render_template('register_user.html')

@users_blueprint.route('/create_user', methods=['POST',])
def create_user():
    _name = request.form['name']
    _email = request.form['email']
    _phone = request.form['phone']
    _password = request.form['password']

    with sql.connect("app/database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO users (email,name,phone,password) VALUES (?,?,?,?)", (_email,_name,_phone,_password))
        con.commit()

    return render_template('index.html')
