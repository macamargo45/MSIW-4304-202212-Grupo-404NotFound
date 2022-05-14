from flask import Flask
from datetime import timedelta

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:cp7MacxF5SxYGwE@database-entrega-1.cxzib8skydkl.us-east-1.rds.amazonaws.com:5432/BlackListBD'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY']='frase-secreta'
    app.config['JWT_ACCESS_TOKEN_EXPIRES']=timedelta(days=1)
    app.config['PROPAGATE_EXCEPTIONS'] = True

    if(app.config['SQLALCHEMY_DATABASE_URI'] == "" or app.config['SQLALCHEMY_DATABASE_URI'] is None):
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:cp7MacxF5SxYGwE@database-entrega-1.cxzib8skydkl.us-east-1.rds.amazonaws.com:5432/BlackListBD"
        
    return app