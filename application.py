from flaskr.views.viewhealthcheck import ViewHealthCheck
from flaskr.views.viewblacklist import ViewBlacklists, ViewBlacklist
from flaskr import create_app
from flask_restful import Api
from flaskr.models.models import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS

application = create_app('default')
app_context = application.app_context()
app_context.push()

db.init_app(application)
db.create_all()

cors = CORS(application)
jwt = JWTManager(application)
api = Api(application)

# Punto de arranque: gunicorn
def gunicorn():
    # Retornar el objeto de la aplicacion
    return application

api.add_resource(ViewHealthCheck, '/api/healthcheck')
api.add_resource(ViewBlacklists, '/api/blacklists')
api.add_resource(ViewBlacklist, '/api/blacklists/<string:blacklist_email>')

if __name__ == "__main__":
    application.run(port = 5000, debug = True)
