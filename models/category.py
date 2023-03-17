#category model
from db import db,ma

class Category(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), unique=True)

  def __init__(self, name):
    self.name = name

class CategorySchema(ma.Schema):
  class Meta:
    fields = ('id', 'name')

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)