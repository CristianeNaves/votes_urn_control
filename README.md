# Projeto de controle de votos de urna
Desenvolvimento de um sistema de controle de votos de urna para trabalhar conceitos
apresentados na materia Banco de Dados, do departamento de Ciência da Computacao(UnB).

* Para instalar o virtualenv:
```
$ sudo apt-get install python-virtualenv
```

* Para criar uma virtualenv (na pasta do projeto):
```
$ python3 -m venv venv
```

* Para ativar o ambiente virtual:
```
$ source venv/bin/activate
```

* configurar o ambiente virtual:

```
$ pip install -r requirements.txt
```

* Para rodar a aplicacao:
```
$ python3 run.py
```

* Iniciar o banco com o arquivo schema.sql:
```
$ from app import init_db
$ init_db()
```

* Podem ocorrer conflitos, principalmente por falta de dependencias.

* Links uteis:
```
$ http://flask.pocoo.org/docs/1.0/installation/#install-install-virtualenv
$ https://medium.com/the-andela-way/how-i-developed-an-api-in-python-using-flask-4e388674f1
$ http://www.patricksoftwareblog.com/using-blueprints-to-organize-your-application/
$ http://www.patricksoftwareblog.com/creating-a-simple-flask-web-application/
$ http://www.patricksoftwareblog.com/how-to-use-virtual-environments-for-python-projects/
```

* Links DB Sqlite3:
```
$ http://flask.pocoo.org/docs/0.12/tutorial/setup/#tutorial-setup
$ http://flask.pocoo.org/docs/1.0/patterns/sqlite3/
$ https://gist.github.com/PolBaladas/07bfcdefb5c1c57cdeb5
$ https://www.tutorialspoint.com/flask/flask_sqlite.htm
$ https://blog.syncano.io/intro-flask-pt-2-creating-writing-databases/
```
