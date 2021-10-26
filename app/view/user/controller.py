from saika.decorator import *

from .decorator import ignore_auth
from .user_view import UserViewController
from .forms import LoginForm, RegisterForm
from .enums import *


@controller('/user')
class User(UserViewController):
    @ignore_auth
    @get
    @post
    @form(LoginForm)
    @rule('/login')
    def login(self):
        if self.request.method != 'POST':
            return self.fetch()
        data = self.form.data.copy()
        data.pop('submit')

        result = self.service_user.login(**data)
        msg = LOGIN_SUCCESS if result else LOGIN_FAILED
        self.flash(*msg)

        if result:
            return self.redirect(self.url_for('portal.index'))
        else:
            return self.fetch()

    @ignore_auth
    @get
    @post
    @form(RegisterForm)
    @rule('/register')
    def register_(self):
        if self.request.method != 'POST':
            return self.fetch()
        data = self.form.data.copy()
        data.pop('submit')

        result = self.service_user.register(**data)
        msg = REGISTER_SUCCESS if result else REGISTER_FAILED
        self.flash(*msg)

        if result:
            return self.redirect(self.url_for('user.login'))
        else:
            return self.fetch()

    @get
    @rule('/logout')
    def logout(self):
        self.service_user.logout()
        return self.redirect(self.url_for('portal.index'))
