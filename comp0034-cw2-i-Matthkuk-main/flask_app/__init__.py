from pathlib import Path
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .config import Config
from dash_app.graphs import create_dash_app

# Sets the project root folder
PROJECT_ROOT = Path(__file__).parent

# Create a global SQLAlchemy object
db = SQLAlchemy()

# Create a global Flask-Marshmallow object
ma = Marshmallow()


def create_app(config_object=Config):
    """Create and configure the Flask app"""
    app = Flask(__name__)

    # See config parameters in config.py
    app.config.from_object(config_object)

    # Uses a helper function to initialise extensions
    initialize_extensions(app)

    # Register the api and main blueprint for the routes in api_routes.py
    from .api_routes import bp, main_bp
    app.register_blueprint(bp)
    app.register_blueprint(main_bp)

    with app.app_context():
        # This is required as you must instantiate the models before marshamallow schemas
        from .models import Matches, Matches1516, Matches1617, Matches1718, Matches1819

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(405, method_not_allowed)
    app.register_error_handler(403, forbidden)
    app.register_error_handler(400, bad_request)

    create_dash_app(app)

    return app


def initialize_extensions(app):
    """Binds extensions to the Flask application instance (app)"""
    # Flask-SQLAlchemy
    db.init_app(app)
    # Flask-Marshmallow
    ma.init_app(app)


def internal_server_error(e):
    return render_template("500.html"), 500


def page_not_found(e):
    return render_template("404.html"), 404


def method_not_allowed(e):
    return render_template('405.html'), 405


def forbidden(e):
    return render_template('403.html'), 403


def bad_request(e):
    return render_template('400.html'), 400
