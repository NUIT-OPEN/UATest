from saika import Service

from app.models.access_log import AccessLog


class AccessLogService(Service):
    def __init__(self):
        super().__init__(AccessLog)
