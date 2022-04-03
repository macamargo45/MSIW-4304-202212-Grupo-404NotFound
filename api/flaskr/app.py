from flaskr.views.viewhealthcheck import ViewHealthCheck
from flaskr.views.viewblacklist import ViewBlacklists, ViewBlacklist
from flaskr import create_app
from flask_restful import Api
from flaskr.models.models import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)
jwt = JWTManager(app)
api = Api(app)

# Punto de arranque: gunicorn
def gunicorn():
    # Retornar el objeto de la aplicacion
    return app

api.add_resource(ViewHealthCheck, '/api/healthcheck')
api.add_resource(ViewBlacklists, '/api/blacklists')
api.add_resource(ViewBlacklist, '/api/blacklists/<string:blacklist_email>')
