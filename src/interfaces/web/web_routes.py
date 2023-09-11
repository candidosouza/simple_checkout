from flask import Flask
from src.interfaces.web.views.product_views import ProductListView


def register_web_routes(app: Flask):

    product_list_view = ProductListView.as_view('product_list')
    app.add_url_rule('/products/', view_func=product_list_view)
