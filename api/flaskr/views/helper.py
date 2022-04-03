from requests import Response, get
from ..models import db

class Helper():
    def handle_exception(self, e):

        rollbackResult = "Se hizo rollback"
        try:
            db.session.rollback()
        except:
            rollbackResult = "Sí se hizo rollback"
            # do nothing as we are trying to rollback even if there are no transactions pending

        errorDescription = '{ "description" : "Error ocurrido con ' + \
            str(e) + '. Además ' + rollbackResult + '." }'
        the_response = Response()
        the_response.code = 500
        the_response.error_type = "Internal Error"
        the_response.status_code = 500
        the_response._content = bytes(errorDescription, 'utf-8')
        the_response.content_type = "application/json"

        return the_response.json()

    def get_client_ip(self):
        ip_address = get('https://api.ipify.org').content.decode('utf8')
        return ip_address
