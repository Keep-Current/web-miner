import pytest


from flask_server.app import create_app
from flask_server.settings import TestConfig


@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)