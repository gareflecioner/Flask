import os

class BaseConfig:
    DEBUG=True
    CSRF=True
    SECRET_KEY='RANDOM_KEEEEEY'
    SQLALCHEMY_DATA_URI="sqlite:///bd.db"
    SQLALCHEMY_TRACK_=MODIFICATION=False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATA_URI="sqlite:///bd.db"

class DevelopmentConfig(BaseConfig):
    
    DEBUG=True
    SQLALCHEMY_DATA_URI="sqlite:///bd.db"

class TestingConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATA_URI="sqlite:///bd.db"