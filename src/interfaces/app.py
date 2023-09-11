from flask import Flask
from src.interfaces.api.routes.product_routes import api_blueprint


def register_routes(app: Flask):
    app.register_blueprint(api_blueprint, url_prefix='/api')
