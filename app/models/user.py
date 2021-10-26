from datetime import datetime

from saika import db
from saika.decorator import model


@model
class User(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    username = db.Column(db.VARCHAR(191), unique=True)
    password = db.Column(db.VARCHAR(255))
    create_time = db.Column(db.DATETIME, default=datetime.now)
    update_time = db.Column(db.DATETIME, onupdate=datetime.now)
