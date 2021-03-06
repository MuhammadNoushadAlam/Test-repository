
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from Security import authenticate, identity
from resources.user import UserSignUp
from resources.item import Item, ItemList
from resources.store import Store,StoreList
application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
application.config['SQLALCHEMY_TRACK-MODIFICATIONS'] = False
application.secret_key = 'jose'
api = Api(application)

@application.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(application, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')

api.add_resource(Item, '/item/<string:name>')

api.add_resource(ItemList, '/items')

api.add_resource(StoreList, '/stores')

api.add_resource(UserSignUp, '/signup')



if __name__ == '__main__':
    from db import db
    db.init_app(application)
    application.run(port=5003, debug=True)
