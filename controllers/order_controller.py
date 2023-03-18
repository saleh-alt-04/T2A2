from flask import Blueprint, request, jsonify
from db import db
from datetime import timedelta
from models.product import *
from models.delivery import *
from models.order import *
order_bp = Blueprint('order', '__name__', url_prefix='/')

# Create a new order
@order_bp.route('/order', methods=['POST'])
def add_order():
    user_id = request.json['user_id']
    product_id = request.json['product_id']
    quantity = request.json['quantity']
    print (user_id)
    #  Check if user exists
    # user = User.query.get(4)
    # if not user:
    #     return jsonify({'message': 'User not found.'}), 404
    

    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found.'}), 404

    new_order = Order(user_id=user_id, product_id=product_id, quantity=quantity)

    db.session.add(new_order)
    db.session.commit()

    return order_schema.jsonify(new_order)


# Get all orders
@order_bp.route('/orders', methods=['GET'])
def get_orders():
    all_orders = Order.query.all()
    result = orders_schema.dump(all_orders)
    return jsonify(result)


# Get single order by ID
@order_bp.route('/order/<id>', methods=['GET'])
def get_order(id):
    order = Order.query.get(id)
    return order_schema.jsonify(order)


# Update an order
@order_bp.route('/order/<id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get(id)

    user_id = request.json['user_id']
    product_id = request.json['product_id']
    quantity = request.json['quantity']

    order.user_id = user_id
    order.product_id = product_id
    order.quantity = quantity

    db.session.commit()

    return order_schema.jsonify(order)


# Delete an order
@order_bp.route('/order/<id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get(id)
    db.session.delete(order)
    db.session.commit()

    return order_schema.jsonify(order)
