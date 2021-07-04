from flask import Blueprint, request, jsonify
from app import mongo
import flask
import json
from bson import json_util

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
    return jsonify(message="success")

@mod.route('/<user_name>',methods=['GET'])
def query_user(user_name):
    user = mongo.db.users.find({'name':user_name})
    json_docs = [json.dumps(doc, default=json_util.default) for doc in user]
    return jsonify(json_docs)