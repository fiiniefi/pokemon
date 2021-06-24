from pytest import fixture
from starlette.testclient import TestClient

from src.poke.conf.app_builder import setup_app


@fixture
def app():
    return setup_app()


@fixture
def api_client(app):
    return TestClient(app)
