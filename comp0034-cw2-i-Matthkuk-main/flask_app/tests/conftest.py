import pytest
from flask_app import create_app, config


@pytest.fixture(scope="session")
def app():
    app = create_app(config.TestConfig)
    yield app


@pytest.fixture(scope="function")
def test_client(app):
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client
