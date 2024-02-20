"""Flask configuration."""
from pathlib import Path

# Sets the project root folder
PROJECT_ROOT = Path(__file__).parent


class Config:
    """Base config."""

    SECRET_KEY = "ayOqW1P4Iy3C4zm-FfLLcA"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(
        PROJECT_ROOT.joinpath("data", "1415.db")
    )
    SQLALCHEMY_BINDS = {'1516': "sqlite:///" + str(
        PROJECT_ROOT.joinpath("data", "1516.db")),
        '1617': "sqlite:///" + str(
        PROJECT_ROOT.joinpath("data", "1617.db")),
        '1718': "sqlite:///" + str(
        PROJECT_ROOT.joinpath("data", "1718.db")),
        '1819': "sqlite:///" + str(
        PROJECT_ROOT.joinpath("data", "1819.db"))
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


class ProdConfig(Config):
    """Production config.

    Not currently implemented.
    """

    pass


class DevConfig(Config):
    """Development config"""

    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True


class TestConfig(Config):
    """Testing config"""

    TESTING = True
    SQLALCHEMY_ECHO = True
    WTF_CSRF_ENABLED = False
    SERVER_NAME = "127.0.0.1:5000"
