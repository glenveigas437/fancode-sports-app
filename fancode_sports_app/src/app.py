from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os


load_dotenv()

APP_ENV = os.getenv('ENV')
db = SQLAlchemy()


if APP_ENV == 'Development':
    doc = '/api-docs'
else:
    doc = '/'

api = Api(prefix="/api")

def register_extensions(app):
    db.init_app(app)
    api.init_app(app)
    with app.app_context():
        db.create_all()


def register_blueprints(app):
    from src.apis import register_urls
    for route in register_urls.URL_CONFIG.urls:
        api.add_resource(route.view, route.get_url_prefix())

def configure_databse(app):
    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    from src.apis import register_models
    register_blueprints(app)
    configure_databse(app)
    return app

