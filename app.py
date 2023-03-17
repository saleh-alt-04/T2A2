from flask import Flask, request, jsonify
from db import db,ma
from models.product import *
from flask_jwt_extended import JWTManager
# from models.user import *
# from models.category import *
# from models.delivery import *
from controllers.product_controllers import *
from controllers.users_controller import *

# from controllers.users_controller import user_bp

from commands import db_commands


import datetime
import os 

# Init app
app = Flask(__name__)
jwt = JWTManager(app)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'my secret key'
# Init db
db.init_app(app)
ma.init_app(app)



app.register_blueprint(db_commands)
app.register_blueprint(product_bp)
app.register_blueprint(user_bp)










@app.before_first_request
def create_tables():
    db.create_all()
# # Create a Product
# @app.route('/product', methods=['POST'])
# def add_product():
#   name = request.json['name']
#   description = request.json['description']
#   price = request.json['price']
#   qty = request.json['qty']

#   new_product = Product(name, description, price, qty)

#   db.session.add(new_product)
#   db.session.commit()

#   return product_schema.jsonify(new_product)

# # Get All Products
# @app.route('/product', methods=['GET'])
# def get_products():
#   all_products = Product.query.all()
#   result = products_schema.dump(all_products)
#   return jsonify(result)

# # Get Single Products
# @app.route('/product/<id>', methods=['GET'])
# def get_product(id):
#   product = Product.query.get(id)
#   return product_schema.jsonify(product)

# # Update a Product
# @app.route('/product/<id>', methods=['PUT'])
# def update_product(id):
#   product = Product.query.get(id)

#   name = request.json['name']
#   description = request.json['description']
#   price = request.json['price']
#   qty = request.json['qty']

#   product.name = name
#   product.description = description
#   product.price = price
#   product.qty = qty

#   db.session.commit()

#   return product_schema.jsonify(product)

# # Delete Product
# @app.route('/product/<id>', methods=['DELETE'])
# def delete_product(id):  
#   product = Product.query.get(id)
#   db.session.delete(product)
#   db.session.commit()

#   return product_schema.jsonify(product)


# #user Routes
# @app.route('/users', methods=['POST'])
# def add_user():
#   username = request.json['username']
#   email = request.json['email']
#   password = request.json['password']

#   new_user = User(username, email, password)

#   db.session.add(new_user)
#   db.session.commit()

#   return user_schema.jsonify(new_user)

# # Get All Users
# @app.route('/users', methods=['GET'])
# def get_users():
#   all_users = User.query.all()
#   result = users_schema.dump(all_users)
#   return jsonify(result)

# # Get Single User
# @app.route('/users/<id>', methods=['GET'])
# def get_user(id):
#   user = User.query.get(id)
#   return user_schema.jsonify(user)

# # Update a User
# @app.route('/users/<id>', methods=['PUT'])
# def update_user(id):
#   user = User.query.get(id)

#   username = request.json['username']
#   email = request.json['email']
#   password = request.json['password']

#   user.username = username
#   user.email = email
#   user.password = password

#   db.session.commit()

#   return user_schema.jsonify(user)

# # Delete User
# @app.route('/users/<id>', methods=['DELETE'])
# def delete_user(id):  
#   user = User.query.get(id)
#   db.session.delete(user)
#   db.session.commit()

#   return user_schema.jsonify(user)


# # Add New Order
# @app.route('/orders', methods=['POST'])
# def add_order():
#   order_id = request.json['order_id']
#   user_id = request.json['user_id']
#   total_price = request.json['total_price']

#   new_order = Order(order_id, user_id, total_price)

#   db.session.add(new_order)
#   db.session.commit()

#   return order_schema.jsonify(new_order)

# # Get All Orders
# @app.route('/orders', methods=['GET'])
# def get_orders():
#   all_orders = Order.query.all()
#   result = orders_schema.dump(all_orders)
#   return jsonify(result)

# # Get Single Order
# @app.route('/orders/<id>', methods=['GET'])
# def get_order(id):
#   order = Order.query.get(id)
#   return order_schema.jsonify(order)

# # Update an Order
# @app.route('/orders/<id>', methods=['PUT'])
# def update_order(id):
#   order = Order.query.get(id)

#   order_id = request.json['order_id']
#   user_id = request.json['user_id']
#   total_price = request.json['total_price']

#   order.order_id = order_id
#   order.user_id = user_id
#   order.total_price = total_price

#   db.session.commit()

#   return order_schema.jsonify(order)

# # Delete Order
# @app.route('/orders/<id>', methods=['DELETE'])
# def delete_order(id):  
#   order = Order.query.get(id)
#   db.session.delete(order)
#   db.session.commit()

#   return order_schema.jsonify(order)


# @app.route('/categories', methods=['POST'])
# def add_category():
#   name = request.json['name']

#   new_category = Category(name)

#   db.session.add(new_category)
#   db.session.commit()

#   return category_schema.jsonify(new_category)

# # Get All Categories
# @app.route('/categories', methods=['GET'])
# def get_categories():
#   all_categories = Category.query.all()
#   result = categories_schema.dump(all_categories)
#   return jsonify(result)

# # Get Single Category
# @app.route('/categories/<id>', methods=['GET'])
# def get_category(id):
#   category = Category.query.get(id)
#   return category_schema.jsonify(category)

# # Update a Category
# @app.route('/categories/<id>', methods=['PUT'])
# def update_category(id):
#   category = Category.query.get(id)

#   name = request.json['name']

#   category.name = name

#   db.session.commit()

#   return category_schema.jsonify(category)

# # Delete Category
# @app.route('/categories/<id>', methods=['DELETE'])
# def delete_category(id):  
#   category = Category.query.get(id)
#   db.session.delete(category)
#   db.session.commit()

#   return category_schema.jsonify(category) 


# @app.route('/deliveries', methods=['POST'])
# def add_delivery():
#   order_id = request.json['order_id']
#   delivery_date = request.json['delivery_date']
#   address = request.json['address']
#   city = request.json['city']
#   state = request.json['state']
#   zipcode = request.json['zipcode']
#   delivery_status = request.json['delivery_status']

#   new_delivery = Delivery(order_id, delivery_date, address, city, state, zipcode, delivery_status)

#   db.session.add(new_delivery)
#   db.session.commit()

#   return delivery_schema.jsonify(new_delivery)

# # Get All Deliveries
# @app.route('/deliveries', methods=['GET'])
# def get_deliveries():
#   all_deliveries = Delivery.query.all()
#   result = deliveries_schema.dump(all_deliveries)
#   return jsonify(result)

# # Get Single Delivery
# @app.route('/deliveries/<id>', methods=['GET'])
# def get_delivery(id):
#   delivery = Delivery.query.get(id)
#   return delivery_schema.jsonify(delivery)

# # Update a Delivery
# @app.route('/deliveries/<id>', methods=['PUT'])
# def update_delivery(id):
#   delivery = Delivery.query.get(id)

#   order_id = request.json['order_id']
#   delivery_date = request.json['delivery_date']
#   address = request.json['address']
#   city = request.json['city']
#   state = request.json['state']
#   zipcode = request.json['zipcode']
#   delivery_status = request.json['delivery_status']

#   delivery.order_id = order_id
#   delivery.delivery_date = delivery_date
#   delivery.address = address
#   delivery.city = city
#   delivery.state = state
#   delivery.zipcode = zipcode
#   delivery.delivery_status = delivery_status

#   db.session.commit()

#   return delivery_schema.jsonify(delivery)

# # Delete Delivery
# @app.route('/deliveries/<id>', methods=['DELETE'])
# def delete_delivery(id):  
#   delivery = Delivery.query.get(id)
#   db.session.delete(delivery)
#   db.session.commit()

#   return delivery_schema.jsonify(delivery)

for route in app.url_map.iter_rules():
    print(route)
# Run Server
if __name__ == '__main__':
  app.run(debug=True)