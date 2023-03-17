from flask_bcrypt import Bcrypt
from flask import Blueprint
from flask import Flask
from models.user import User
from db import db


app = Flask(__name__)
db_commands = Blueprint('db', __name__)
bcrypt = Bcrypt(app)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print('Tables created')

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')


#seeds tables
def seed_db():

    users = [
        User(
            username = 'test1',
            email = 'test1',
            password = bcrypt.generate_password_hash('test1').decode('utf-8'),
            is_admin = True
        ),
        User(
            username = 'test2',
            email = 'test2',
            password = bcrypt.generate_password_hash('test2').decode('utf-8'),
            is_admin = False

        ),

    ]
   

    db.session.add_all(users)
    db.session.commit()



    print('Tables seeded')