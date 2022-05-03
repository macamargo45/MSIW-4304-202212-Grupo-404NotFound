from flask_restful import Resource

class ViewDefault(Resource):

    def get(self):
        return "OK default"
