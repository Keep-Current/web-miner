import pytest


from webminer.external_interfaces.flask_server.app import create_app
from webminer.external_interfaces.flask_server.settings import TestConfig


@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)