from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class Blacklist(db.Model):
    __tablename__ = 'Blacklist'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    app_uuid = db.Column(db.String(100))
    blocked_reason = db.Column(db.Text())
    ip =  db.Column(db.String(100))
    created_at = db.Column(db.DateTime())

    def __init__(self, email, app_uuid, blocked_reason, ip, created_at):
        self.email = email
        self.app_uuid = app_uuid,
        self.blocked_reason = blocked_reason
        self.ip = ip
        self.created_at = created_at

    def __repr__(self):
        return '<id {}>'.format(self.id)


class BlacklistSimpleSchema(SQLAlchemyAutoSchema):
    class Meta:
         fields = ('id','email', 'app_uuid', 'blocked_reason', 'ip', 'created_at')
         include_relationships = True
         load_instance = True

class BlacklistSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Blacklist
         include_relationships = True
         load_instance = True