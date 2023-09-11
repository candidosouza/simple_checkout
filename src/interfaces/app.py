from flask import Flask
from src.interfaces.api.routes.product_routes import api_blueprint
from src.interfaces.web.views.product_views import ProductListView


def register_routes(app: Flask):
    app.register_blueprint(api_blueprint, url_prefix='/api')

    product_list_view = ProductListView.as_view('product_list')
    app.add_url_rule('/products/', view_func=product_list_view)
