# Order Model
from db import db,ma

class Order(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  order_id = db.Column(db.String(50), unique=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  total_price = db.Column(db.Float, nullable=False)

  def __init__(self, order_id, user_id, total_price):
    self.order_id = order_id
    self.user_id = user_id
    self.total_price = total_price

class OrderSchema(ma.Schema):
  class Meta:
    fields = ('id', 'order_id', 'user_id', 'order_date', 'total_price')

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)