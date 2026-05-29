import os

class Config:

    SECRET_KEY = "secret"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):

    SQLALCHEMY_DATABASE_URI = "sqlite:///data.sqlite"


class TestingConfig(Config):

    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

    TESTING = True

    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):

    SQLALCHEMY_DATABASE_URI = "sqlite:///data.sqlite"