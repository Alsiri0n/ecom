from flask import Flask
from config import DevelopmentConfig, ProductionConfig, TestingConfig
from pymongo import MongoClient

profiles = {
    "development": DevelopmentConfig(),
    "production": ProductionConfig(),
    "testing": TestingConfig()
}

# client = MongoClient()


def create_app(profile) -> Flask:
    """
    Create app and loading config
    :param profile: dev prod or test profile
    :return: app flask
    """
    app = Flask(__name__)
    app.config.from_object(profiles[profile])
    client = MongoClient(app.config["MONGO_URI"])
    app.db = client["app"]

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
