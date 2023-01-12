"""
This module create all env variables for application
"""
import os


class Config(object):
    """
    Config for loading constants from env or default values
    """
    pass


class ProductionConfig(Config):
    FLASK_HOST = os.environ.get('FLASK_HOST')
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
    MONGO_URI = os.environ.get('MONGO_URL')


class DevelopmentConfig(Config):
    FLASK_HOST = os.environ.get('FLASK_HOST') or '127.0.0.1'
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT') or '6000'
    MONGO_URI = os.environ.get('MONGO_URL')


class TestingConfig(Config):
    TESTING = True
