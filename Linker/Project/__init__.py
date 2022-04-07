from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_bootstrap import Bootstrap


app = Flask('Linker')

app.config.from_pyfile('config.py')

bootstrap = Bootstrap(app)

db = SQLAlchemy(app)


from Linker import commands,errors,views,login

