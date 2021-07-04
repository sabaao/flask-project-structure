from flask import Blueprint, request
from app import mongo
import flask

mod = Blueprint('users', __name__, url_prefix='/users')

@mod.route('/',methods=['GET'])
def index():
    return 'hello world'

@mod.route('/',methods=['POST'])
def add_users():
    content = request.get_json()
    user = {
        "name":content.name,
        "age":content.age
    }
    mongo.db.users.insert_one(user)
    return flask.jsonify(message="success")