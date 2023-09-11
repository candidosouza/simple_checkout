from flask import jsonify


def serialize_product(product):
    return {
        'id': product['id'],
        'name': product['name'],
        'price': product['price'],
        'status': product['status']
    }
    # return {
    #     'name': product.name,
    #     'price': product.price,
    #     'status': product.status.value
    # }

def deserialize_products(request):
    data = request.json
    return {
        'name': data.get('name'),
        'price': data.get('price'),
        'status': data.get('status')
    }
