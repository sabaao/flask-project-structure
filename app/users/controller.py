from flask import Blueprint

mod = Blueprint('users', __name__, url_prefix='/users')

@mod.route('/',methods=['GET'])
def index():
    return 'hello world'