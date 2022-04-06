from distutils.command.config import config
from distutils.debug import DEBUG

class DevelopmentConfig():
    DEBUG = True
    MYQSL_HOST = 'localhost'
    MYSQL_USER = 'drestrepo'
    MYSQL_PASSWORD = '123'
    MYSQL_DB = 'api-flask'


config = {
    'development': DevelopmentConfig
}
