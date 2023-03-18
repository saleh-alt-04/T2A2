# Product Class/Model
from db import db,ma
from marshmallow import fields
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  description = db.Column(db.String(200))
  price = db.Column(db.Float)
  qty = db.Column(db.Integer)
  category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
  category = db.relationship('Category', backref=db.backref('products', lazy=True))

  def __init__(self, name, description, price, qty,category_id):
    self.name = name
    self.description = description
    self.price = price
    self.qty = qty
    self.category_id=category_id

# Product Schema
class ProductSchema(ma.Schema):
  category_name = fields.String(attribute='category.name')
 
  class Meta:
    fields = ('id', 'name', 'description', 'price', 'qty','category_name')
    
    

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)