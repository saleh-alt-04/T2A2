from flask import Blueprint, request, jsonify
from db import db
from datetime import timedelta
from models.product import *
from models.delivery import *
from models.order import *
from datetime import datetime


delivery_bp = Blueprint('delivery', '__name__', url_prefix='/')
# Create a new delivery
@delivery_bp.route('/delivery', methods=['POST'])
def add_delivery():
    order_id = request.json['order_id']
    delivery_date_str = request.json['delivery_date']
    delivery_date = datetime.strptime(delivery_date_str, '%Y-%m-%d').date()
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zipcode']
    delivery_status = "pending"
    order = Order.query.filter_by(id=order_id).first()
    if order is None:
        return jsonify("Order doesn't exist")
    new_delivery = Delivery(order_id, delivery_date, address, city, state, zipcode, delivery_status)

    db.session.add(new_delivery)
    db.session.commit()

    return delivery_schema.jsonify(new_delivery)


# Get all deliveries
@delivery_bp.route('/delivery', methods=['GET'])
def get_deliveries():
    all_deliveries = Delivery.query.all()
    result = deliveries_schema.dump(all_deliveries)
    return jsonify(result)


# Get a single delivery by ID
@delivery_bp.route('/delivery/<id>', methods=['GET'])
def get_delivery(id):
    delivery = Delivery.query.get(id)
    return delivery_schema.jsonify(delivery)


# Update a delivery by ID
@delivery_bp.route('/delivery/<id>', methods=['PUT'])
def update_delivery(id):
    delivery = Delivery.query.get(id)

    order_id = request.json['order_id']
    delivery_date = request.json['delivery_date']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zipcode']
    delivery_status = request.json['delivery_status']

    delivery.order_id = order_id
    delivery.delivery_date = delivery_date
    delivery.address = address
    delivery.city = city
    delivery.state = state
    delivery.zipcode = zipcode
    delivery.delivery_status = delivery_status

    db.session.commit()

    return delivery_schema.jsonify(delivery)


# Delete a delivery by ID
@delivery_bp.route('/delivery/<id>', methods=['DELETE'])
def delete_delivery(id):
    delivery = Delivery.query.get(id)
    db.session.delete(delivery)
    db.session.commit()

    return delivery_schema.jsonify(delivery)
