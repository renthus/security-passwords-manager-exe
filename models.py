from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///password.db'
app.config['SQLALCHEMY_ECHO']=True

db = SQLAlchemy(app)

class Password_Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String, nullable=False, unique=True)
    login = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, name, address, login, password):
        self.name = name
        self.address = address
        self.login = login
        self.password = password

## -- recriar banco de dados
db.drop_all()
db.create_all()