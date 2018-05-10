from flask import Flask

from flask_server.rest import arxiv_document
from flask_server.settings import DevConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(arxiv_document.blueprint)
    return app