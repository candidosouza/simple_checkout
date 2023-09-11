from flask import Blueprint, request, jsonify
from src.interfaces.api.serializers.product_serializers import serialize_product, deserialize_products


api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/products', methods=['GET'])
def get_products():
    items = [
        {
            'id': 1,
            'name': 'Item 1',
            'price': 10.0,
            'status': 'enabled'
        }
    ]
    return jsonify([serialize_product(item) for item in items])


# @api_blueprint.route('/products/<int:product_id>', methods=['GET'])
# def get_product(product_id):
#     product = product_repo.get_by_id(product_id)
#     if not product:
#         return jsonify({'error': 'Product not found'}), 404
#     return jsonify(serialize_product(product))


# @api_blueprint.route('/products', methods=['POST'])
# def create_product():
#     product_data = deserialize_products(request)
#     product = Product(**product_data)
#     product_repo.save(product)
#     return jsonify(serialize_product(product)), 201
