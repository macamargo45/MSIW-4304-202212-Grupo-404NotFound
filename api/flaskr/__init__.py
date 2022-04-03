from flask import Flask
from datetime import timedelta
import os

def create_app(config_name):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_HOST')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY']='frase-secreta'
    app.config['JWT_ACCESS_TOKEN_EXPIRES']=timedelta(days=1)
    app.config['PROPAGATE_EXCEPTIONS'] = True

    if(app.config['SQLALCHEMY_DATABASE_URI'] == "" or app.config['SQLALCHEMY_DATABASE_URI'] is None):
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:changeme@localhost:5433/BlackListBD"
        
        
    return app