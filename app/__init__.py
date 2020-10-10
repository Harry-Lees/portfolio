from flask import Flask

def create_app() -> object:
    app = Flask(__name__)

    app.config.from_object('config.DevelopmentConfig')

    from .core.routes import blueprint as core_bp
    app.register_blueprint(core_bp)

    return app