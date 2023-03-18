from flask import Flask, request, jsonify
from db import db,ma
from models.product import *
from flask_jwt_extended import JWTManager
from controllers.product_controllers import *
from controllers.users_controller import *
from controllers.category_controller import *
from controllers.order_controller import *
from controllers.delivery_controller import *




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
app.register_blueprint(category_bp)
app.register_blueprint(order_bp)
app.register_blueprint(delivery_bp)







@app.before_first_request
def create_tables():
    db.create_all()


for route in app.url_map.iter_rules():
    print(route)
# Run Server
if __name__ == '__main__':
  app.run(debug=True)