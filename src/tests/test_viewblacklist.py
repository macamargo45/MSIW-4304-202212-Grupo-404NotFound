import unittest
import json

from src.models import db,Blacklist
from application import application

class ViewBlacklistsTetCase(unittest.TestCase):
  
  
  def setUp(self):
    
    self.client = application.test_client()
    # Crea un contexto de aplicación
    application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:DbPru3b45Unni7735@devops-pruebas-unitarias.csspjbx1sxg8.us-east-1.rds.amazonaws.com:5432/postgres'
    application.config['TESTING'] = True
    application.config['WTF_CSRF_ENABLED'] = False
    application.config['DEBUG'] = False
    with application.app_context():
      # Crea las tablas de la base de datos
      db.init_app(application)
      db.create_all()
    
  
  def test_consult_email_registered(self):

    email= "andres-unittest@uniandes.edu.co"
    
    email_register = Blacklist(email=email,app_uuid="ASDFVGYHNMJIKLOPIGG",blocked_reason="El usuario usa lenguaje violento y grosero contra otros usuarios.",ip="184.4.0.160",created_at="2022-04-03 13:59:10.307")
    db.session.add(email_register)
    db.session.commit()
        
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2NDg5NDMzMTAsImV4cCI6MTY4MDQ3OTMxMCwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSIsIkdpdmVuTmFtZSI6IkpvaG5ueSIsIlN1cm5hbWUiOiJSb2NrZXQiLCJFbWFpbCI6Impyb2NrZXRAZXhhbXBsZS5jb20iLCJSb2xlIjpbIk1hbmFnZXIiLCJQcm9qZWN0IEFkbWluaXN0cmF0b3IiXX0.MpR0dkXB5zadTI-4FEYV5pr4ofx5e7IJkmJdTsgrrG8"
    addEmailResponse = self.client.get(f'api/blacklists/{email}',content_type='application/json', headers=dict(Authorization='Bearer {0}'.format(token)))
    self.assertEqual(addEmailResponse.status_code, 200)

  def test_consult_email_unregistered(self):

    email= "andres-unittest@uniandes.edu.co"
    
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2NDg5NDMzMTAsImV4cCI6MTY4MDQ3OTMxMCwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSIsIkdpdmVuTmFtZSI6IkpvaG5ueSIsIlN1cm5hbWUiOiJSb2NrZXQiLCJFbWFpbCI6Impyb2NrZXRAZXhhbXBsZS5jb20iLCJSb2xlIjpbIk1hbmFnZXIiLCJQcm9qZWN0IEFkbWluaXN0cmF0b3IiXX0.MpR0dkXB5zadTI-4FEYV5pr4ofx5e7IJkmJdTsgrrG8"
    addEmailResponse = self.client.get(f'api/blacklists/{email}',content_type='application/json', headers=dict(Authorization='Bearer {0}'.format(token)))
    self.assertEqual(addEmailResponse.status_code, 500)

  def test_consult_email_bad_token(self):

    email= "andres-unittest@uniandes.edu.co"
    
    email_register = Blacklist(email=email,app_uuid="ASDFVGYHNMJIKLOPIGG",blocked_reason="El usuario usa lenguaje violento y grosero contra otros usuarios.",ip="184.4.0.160",created_at="2022-04-03 13:59:10.307")
    db.session.add(email_register)
    db.session.commit()
        
    token = "bad_token"
    addEmailResponse = self.client.get(f'api/blacklists/{email}',content_type='application/json', headers=dict(Authorization='Bearer {0}'.format(token)))
    self.assertEqual(addEmailResponse.status_code, 200)

  def tearDown(self):
    with application.app_context():
      # Elimina todas las tablas de la base de datos
      db.session.remove()
      db.drop_all()
