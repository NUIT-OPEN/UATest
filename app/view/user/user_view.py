from saika import MetaTable, ViewController
from saika.context import Context

from app.models.user import User
from .enums import *
from .hard_code import *


class UserViewController(ViewController):
    @property
    def service_user(self):
        from .service import UserService
        return UserService()

    def callback_before_register(self):
        super().callback_before_register()

        @self.blueprint.before_request
        def authentication():
            f = Context.get_view_function()
            if f is None or MetaTable.get(f, MK_PUBLIC):
                return

            user = self.context.session.get(SK_USER)
            if user is None:
                self.flash(*PERMISSION_DENIED)
                return self.redirect(self.url_for('user.login'))

            self.context.g_set(GK_USER, user)

    @property
    def current_user(self):
        user = self.context.g_get(GK_USER)  # type: User
        return user
