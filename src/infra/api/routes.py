from flask import Blueprint, jsonify


api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/', methods=['GET'])
def get_products():
    items = [
        {
            'id': 1,
            'name': 'Item 1',
            'price': 10.0,
            'status': 'enabled'
        }
    ]
    return jsonify(items)
