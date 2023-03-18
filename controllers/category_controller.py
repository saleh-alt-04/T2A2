from flask import Blueprint, request, jsonify
from db import db
from datetime import timedelta
from models.product import *
from models.category import *

category_bp = Blueprint('category', '__name__', url_prefix='/')

# Get All Categories
@category_bp.route('/categories', methods=['GET'])
def get_categories():
  all_categories = Category.query.all()
  result = categories_schema.dump(all_categories)
  return jsonify(result)

# Get Single Category
@category_bp.route('/categories/<id>', methods=['GET'])
def get_category(id):
  category = Category.query.get(id)
  return category_schema.jsonify(category)

# Update a Category
@category_bp.route('/categories/<id>', methods=['PUT'])
def update_category(id):
  category = Category.query.get(id)

  name = request.json['name']

  category.name = name

  db.session.commit()

  return category_schema.jsonify(category)

# Delete Category
@category_bp.route('/categories/<id>', methods=['DELETE'])
def delete_category(id):  
  category = Category.query.get(id)
  db.session.delete(category)
  db.session.commit()

  return category_schema.jsonify(category) 
