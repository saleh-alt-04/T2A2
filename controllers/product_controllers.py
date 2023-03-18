from flask import Blueprint, request, jsonify
from db import db
from datetime import timedelta
from models.product import *
from models.category import Category


product_bp = Blueprint('products', '__name__', url_prefix='/')

# Create a Product
@product_bp.route('/product', methods=['POST'])
def add_product():
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']
  category_id = request.json['category_id']

  new_product = Product(name, description, price, qty,category_id)

  db.session.add(new_product)
  db.session.commit()

  return product_schema.jsonify(new_product)

# Get All Products
@product_bp.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.join(Category).all()
    result = products_schema.dump(all_products)
    print (result)    
    return jsonify(result)

# Get Single Products
@product_bp.route('/product/<id>', methods=['GET'])
def get_product(id):
  product = Product.query.get(id)
  return product_schema.jsonify(product)

# Update a Product
@product_bp.route('/product/<id>', methods=['PUT'])
def update_product(id):
  product = Product.query.get(id)

  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  product.name = name
  product.description = description
  product.price = price
  product.qty = qty

  db.session.commit()

  return product_schema.jsonify(product)

# Delete Product
@product_bp.route('/product/<id>', methods=['DELETE'])
def delete_product(id):  
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return product_schema.jsonify(product)
