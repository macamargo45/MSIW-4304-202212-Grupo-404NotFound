import jwt
from .helper import Helper
from flask import request
from ..models import Blacklist, BlacklistSchema, BlacklistSimpleSchema
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from ..models import db
from datetime import datetime
import os

blacklist_schema = BlacklistSchema()
blacklist_simple_schema = BlacklistSimpleSchema()
helper = Helper()


class ViewBlacklists(Resource):
    @jwt_required()
    def get(self):
        try:
            blacklists = Blacklist.query.all()
            return [blacklist_schema.dump(bl) for bl in blacklists], 200
        except BaseException as err:
            return helper.handle_exception(err)

    @jwt_required()
    def post(self):
        try:
            exist_email = Blacklist.query.filter(Blacklist.email == request.json["email"]).first()
            if(exist_email):
                return helper.handle_exception("Email ya registrado")

            blacklist = Blacklist(
                email=request.json["email"],
                app_uuid=request.json["app_uuid"],
                blocked_reason=request.json["blocked_reason"],
                ip=helper.get_client_ip(),
                created_at=datetime.now()
            )

            db.session.add(blacklist)
            db.session.commit()
            db.session.refresh(blacklist)

            return blacklist_schema.dump(blacklist), 200
        except BaseException as err:
            return helper.handle_exception(err)


class ViewBlacklist(Resource):
    @jwt_required()
    def get(self, blacklist_email):
        try:
            print ("EMAIL:", blacklist_email)
            tarea = Blacklist.query.filter(Blacklist.email == blacklist_email).one()
            return blacklist_schema.dump(tarea), 200
        except BaseException as err:
            return helper.handle_exception(err)
