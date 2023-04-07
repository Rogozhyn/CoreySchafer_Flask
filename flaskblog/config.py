import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = eval(os.environ.get('SQLALCHEMY_DB_URI'))
    # eval() doesn't work by using supervisor, although direct with gunicorn it works
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'site.db')
    MAIL_SERVER = os.environ.get('EMAIL_SERV')
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'default': Config,
    'development': DevelopmentConfig,
}
