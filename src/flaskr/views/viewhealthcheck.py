from flask_restful import Resource
from .helper import Helper

helper = Helper()

class ViewHealthCheck(Resource):
    
    def get(self):
        try:
            return {
                "mensaje":"Endpoint activo"
            },200
        except Exception as err:
            return helper.handle_exception(err)


    