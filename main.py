from flask import Flask
from src.interfaces.api.api_routes import register_api_routes
from src.interfaces.web.web_routes import register_web_routes
from config import DevelopmentConfig


def create_app():
    app = Flask(__name__,
                template_folder=DevelopmentConfig.TEMPLATE_FOLDER,
                static_folder=DevelopmentConfig.STATIC_FOLDER)
    app.config.from_object(DevelopmentConfig)

    register_api_routes(app)
    register_web_routes(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8000, debug=True)
