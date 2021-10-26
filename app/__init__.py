from saika import SaikaApp
from flask_bootstrap import Bootstrap


class Application(SaikaApp):
    def callback_init_app(self):
        self.jinja_env.add_extension('jinja2.ext.loopcontrols')
        bootstrap.init_app(self)


bootstrap = Bootstrap()
app = Application()
