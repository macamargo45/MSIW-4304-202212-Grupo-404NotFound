import unittest
import json

from flaskr.models import db,Blacklist
from application import application

class ViewBlacklistsTestCase(unittest.TestCase):
  
  
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
    
  def test_add_email_to_blacklist(self):

    data ={
      "email": "andres-unittest@uniandes.edu.co",
      "app_uuid": "jsaghkjashsajkahskasj",
      "blocked_reason": "No respeta las normas de la comunidad"
    }
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2NDg5NDMzMTAsImV4cCI6MTY4MDQ3OTMxMCwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSIsIkdpdmVuTmFtZSI6IkpvaG5ueSIsIlN1cm5hbWUiOiJSb2NrZXQiLCJFbWFpbCI6Impyb2NrZXRAZXhhbXBsZS5jb20iLCJSb2xlIjpbIk1hbmFnZXIiLCJQcm9qZWN0IEFkbWluaXN0cmF0b3IiXX0.MpR0dkXB5zadTI-4FEYV5pr4ofx5e7IJkmJdTsgrrG8"

    addEmailResponse = self.client.post('api/blacklists', data=json.dumps(dict(data)),content_type='application/json', headers=dict(Authorization='Bearer {0}'.format(token)))
    self.assertEqual(addEmailResponse.status_code, 200)

  def test_bad_token(self):

    data ={
      "email": "andres-unittest@uniandes.edu.co",
      "app_uuid": "jsaghkjashsajkahskasj",
      "blocked_reason": "No respeta las normas de la comunidad"
    }
    token = "This_is_not_a _token"

    addEmailResponse = self.client.post('api/blacklists', data=json.dumps(dict(data)),content_type='application/json', headers=dict(Authorization='Bearer {0}'.format(token)))
    self.assertEqual(addEmailResponse.status_code, 422)

  def test_email_registrado(self):

    email_register = Blacklist(email="andres-unittest@uniandes.edu.co",app_uuid="ASDFVGYHNMJIKLOPIGG",blocked_reason="El usuario usa lengiaje violento y grosero contra otros usuarios.",ip="184.4.0.160",created_at="2022-04-03 13:59:10.307")
    db.session.add(email_register)
    db.session.commit()

    data ={
      "email": "andres-unittest@uniandes.edu.co",
      "app_uuid": "jsaghkjashsajkahskasj",
      "blocked_reason": "No respeta las normas de la comunidad"
    }
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2NDg5NDMzMTAsImV4cCI6MTY4MDQ3OTMxMCwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSIsIkdpdmVuTmFtZSI6IkpvaG5ueSIsIlN1cm5hbWUiOiJSb2NrZXQiLCJFbWFpbCI6Impyb2NrZXRAZXhhbXBsZS5jb20iLCJSb2xlIjpbIk1hbmFnZXIiLCJQcm9qZWN0IEFkbWluaXN0cmF0b3IiXX0.MpR0dkXB5zadTI-4FEYV5pr4ofx5e7IJkmJdTsgrrG8"
    addEmailResponse = self.client.post('api/blacklists', data=json.dumps(dict(data)),content_type='application/json', headers=dict(Authorization='Bearer {0}'.format(token)))
    self.assertEqual(addEmailResponse.status_code, 500)

  def tearDown(self):
    with application.app_context():
      # Elimina todas las tablas de la base de datos
      db.session.remove()
      db.drop_all()