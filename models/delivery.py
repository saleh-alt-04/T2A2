#delivery model
from db import db,ma
import datetime

class Delivery(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
  delivery_date = db.Column(db.Date)
  address = db.Column(db.String(100))
  city = db.Column(db.String(50))
  state = db.Column(db.String(50))
  zipcode = db.Column(db.Integer)
  delivery_status = db.Column(db.String(20))

  def __init__(self, order_id, delivery_date, address, city, state, zipcode, delivery_status):
    self.order_id = order_id
    self.delivery_date = delivery_date
    self.address = address
    self.city = city
    self.state = state
    self.zipcode = zipcode
    self.delivery_status = delivery_status

class DeliverySchema(ma.Schema):
  class Meta:
    fields = ('id', 'order_id', 'delivery_date', 'address', 'city', 'state', 'zipcode', 'delivery_status')

delivery_schema = DeliverySchema()
deliveries_schema = DeliverySchema(many=True)