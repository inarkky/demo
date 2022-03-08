"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment


def create_app():
    """Construct core Flask app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = Environment()
    assets.init_app(app)

    # Initialize plugins
    assets.init_app(app)

    with app.app_context():
        # Import parts of our flask_assets_tutorial
        from .blueprints.currency import currency_routes
        # from .assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(currency_routes.currency_bp)

        # Compile static assets
        # compile_static_assets(assets)

        return app