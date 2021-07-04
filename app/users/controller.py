from flask import Blueprint, request
from app import mongo

mod = Blueprint('users', __name__, url_prefix='/users')

@mod.route('/',methods=['GET'])
def index():
    return 'hello world'

@mod.route('/',methods=['POST'])
def add_users():
    content = request.get_json()
    print(content)
    mongo.db.users.insert_one(content)
    return {"success":True}