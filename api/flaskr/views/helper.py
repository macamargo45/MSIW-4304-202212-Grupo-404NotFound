from requests import Response, get
from ..models import db

class Helper():
    def handle_exception(self, e):

        rollbackResult = "se hizo rollback"
        try:
            db.session.rollback()
        except:
            rollbackResult = "no se hizo rollback"
            # do nothing as we are trying to rollback even if there are no transactions pending

        errorDescription = '{ "description" : "Error ocurrido: ' + \
            str(e) + '. Además ' + rollbackResult + '." }'
        the_response = Response()
        the_response.error_type = "Internal Error"
        the_response._content = bytes(errorDescription, 'utf-8')
        the_response.content_type = "application/json"

        return the_response.json(), 500

    def get_client_ip(self):
        ip_address = get('https://api.ipify.org').content.decode('utf8')
        return ip_address
