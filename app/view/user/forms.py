from saika.form import Form, simple_choices
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('登录')


class RegisterForm(LoginForm):
    submit = SubmitField('注册')


class ChangePasswordForm(Form):
    old = PasswordField('旧密码', validators=[DataRequired()])
    new = PasswordField('新密码', validators=[DataRequired()])
    submit = SubmitField('提交')
