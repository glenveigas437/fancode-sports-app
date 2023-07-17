import os
import enum


class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REMEMBER_COOKIE_DURATION = 3600

    # DATABASE URI
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}/{}'.format(
        os.getenv('DIALECT'),
        os.getenv('DB_USERNAME'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_HOST'),
        os.getenv('DB_NAME')
    )

class DebugConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI =  '{}://{}:{}@{}/{}'.format(
        os.getenv('DIALECT'),
        os.getenv('DB_USERNAME'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_HOST'),
        os.getenv('TEST_DB')
    )
    

config_dict = {
    'Debug': DebugConfig,
    'Testing': TestingConfig
}
