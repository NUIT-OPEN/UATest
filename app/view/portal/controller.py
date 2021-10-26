from pyecharts.charts import Bar, Pie
from saika import db
from saika.decorator import *

from .service import AccessLogService
from ..user.decorator import ignore_auth
from ...models.access_log import AccessLog
from app.view.user.user_view import UserViewController

SK_STATISTIC = 'statistic'
SSK_LOG_ID = 'log_id'
SSK_COUNT = 'count'


@controller('/')
class Portal(UserViewController):
    @property
    def service_log(self):
        return AccessLogService()

    @ignore_auth
    @rule('/')
    @get
    def index(self):
        sess = self.context.session
        req = self.request

        statistic = sess.get(SK_STATISTIC)
        if statistic is None:
            ua = req.user_agent
            log = self.service_log.add(
                browser=ua.browser,
                platform=ua.platform,
            )  # type: AccessLog
            sess[SK_STATISTIC] = {
                SSK_LOG_ID: log.id,
                SSK_COUNT: 1,
            }
        else:
            statistic[SSK_COUNT] += 1
            sess[SK_STATISTIC] = statistic
            self.service_log.edit(statistic[SSK_LOG_ID], count=statistic[SSK_COUNT])
            log = self.service_log.filters(id=statistic[SSK_LOG_ID]).get_one()

        count = dict(
            user_reg=self.service_user.query.count(),
            user=self.service_log.query.count(),
            access=db.query(db.func.sum(AccessLog.count)).scalar(),
        )

        charts = dict(
            pie_1=Pie().add(
                '浏览器用户群体分析', db.query(AccessLog.browser, db.func.count('*')).group_by(
                    AccessLog.browser).all()).render_notebook(),
            pie_2=Pie().add(
                '操作系统用户群体分析', db.query(AccessLog.platform, db.func.count('*')).group_by(
                    AccessLog.platform).all()).render_notebook(),
        )

        self.assign(log=log, count=count, charts=charts)

        return self.fetch()
