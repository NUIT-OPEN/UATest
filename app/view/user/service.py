import hashlib

from saika import db, common, Service, Config, Context
from .hard_code import *
from app.models.user import User


class UserService(Service):
    def __init__(self):
        super().__init__(User)

    @staticmethod
    def pw_hash(x: str):
        return hashlib.md5(x.encode()).hexdigest()

    def register(self, username, password):
        item = self.filters(username=username).get_one()
        if item is not None:
            return False

        password = self.pw_hash(password)
        item = self.add(
            username=username,
            password=password,
        )  # type: User

        return item

    def login(self, username, password):
        password = self.pw_hash(password)
        item = self.query.filter_by(
            username=username,
            password=password,
        ).first()  # type: User

        if item is None:
            return False
        else:
            Context.session[SK_USER] = db.dump_instance(
                item, User.id, User.username)
            return True

    def logout(self):
        Context.session.pop(SK_USER)

    def change_password(self, username, old, new):
        password = self.pw_hash(old)
        item = self.query.filter_by(
            username=username,
            password=password,
        ).first()  # type: User

        if item is None:
            return False
        else:
            item.password = self.pw_hash(new)
            db.add_instance(item)
            return True
