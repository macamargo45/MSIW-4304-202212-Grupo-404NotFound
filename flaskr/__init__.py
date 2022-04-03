from flask import Flask
from datetime import timedelta
import os

def create_app(config_name):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:SXG0n2BHHnkOOWrxseMh@db-devops.cew5sozmzl0x.us-east-1.rds.amazonaws.com:5432/entrega1"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY']='frase-secreta'
    app.config['JWT_ACCESS_TOKEN_EXPIRES']=timedelta(days=1)
    app.config['PROPAGATE_EXCEPTIONS'] = True

    if(app.config['SQLALCHEMY_DATABASE_URI'] == "" or app.config['SQLALCHEMY_DATABASE_URI'] is None):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///entrega1.db"
        
        
    return app
