from flask import Flask
from src.interfaces.app import register_routes


def create_app():
    app = Flask(
        __name__,
        template_folder='src/interfaces/web/templates',
        static_folder='src/interfaces/web/static'
        )
    register_routes(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8000, debug=True)