import pymysql
from api.project_1.config.config import Config


class DbUtil(object):
    def __init__(self):
        self.conn = pymysql.connect(host=Config.service_host_test, user=Config.db_user, password=Config.db_password,
                                    database=Config.db, autocommit=True)
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
