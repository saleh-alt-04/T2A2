# Order Model
from db import db,ma
from models.user import *
from models.product import *
from models.delivery import *
from models.user import *
from models.order import *


class Order(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
  quantity = db.Column(db.Integer)
  

  user = db.relationship('User', backref=db.backref('orders', lazy=True))
  product = db.relationship('Product', backref=db.backref('orders', lazy=True))

  def __init__(self, user_id, product_id,quantity):
    self.user_id = user_id
    self.product_id = product_id
    self.quantity = quantity

class OrderSchema(ma.Schema):
  class Meta:
    fields = ('id', 'user_id', 'product_id', 'quantity',)

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)