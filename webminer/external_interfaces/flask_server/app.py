"""It creates the flask server with an environment and returns the server"""

from flask import Flask

from webminer.external_interfaces.flask_server.rest import arxiv_document
from webminer.external_interfaces.flask_server.settings import DevConfig


def create_app(config_object=DevConfig):
    """Creates the server

    Args:
        config_object (object, optional): Defaults to DevConfig.
            Adds a config when creating the app server

    Returns:
        class 'flask.app.Flask': A Flask app
    """

    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(arxiv_document.blueprint)
    return app
