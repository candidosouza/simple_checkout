from flask.views import View
from flask import render_template, request, redirect, url_for

products = []

class ProductListView(View):

    def dispatch_request(self):
        return render_template('products/list.html', products=products)