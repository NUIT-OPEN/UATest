from saika.database import db
from saika.decorator import model


@model
class AccessLog(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    browser = db.Column(db.VARCHAR(191), index=True)
    platform = db.Column(db.VARCHAR(191), index=True)
    count = db.Column(db.INTEGER)
