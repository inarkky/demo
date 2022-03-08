"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session


db = SQLAlchemy()
login_manager = LoginManager()
sess = Session()


def create_app():
    """Construct core Flask app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = Environment()

    # Initialize plugins
    assets.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    sess.init_app(app)

    with app.app_context():
        # Import blueprints
        from . import auth
        from .blueprints.main import main
        from .blueprints.transactions import transaction
        from .assets import compile_static_assets, compile_auth_assets

        app.register_blueprint(main.main_bp)
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(transaction.transaction_bp)

        # Create static asset bundles
        compile_static_assets(app)
        compile_auth_assets(app)

        # Create Database Models
        db.create_all()

        return app