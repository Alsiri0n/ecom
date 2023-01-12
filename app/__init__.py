from flask import Flask
from config import DevelopmentConfig, ProductionConfig, TestingConfig

profiles = {
    "development": DevelopmentConfig(),
    "production": ProductionConfig(),
    "testing": TestingConfig()
}


def create_app(profile) -> Flask:
    """
    Create app and loading config
    :param profile: dev prod or test profile
    :return: app flask
    """
    app = Flask(__name__)
    app.config.from_object(profiles[profile])

    return app
