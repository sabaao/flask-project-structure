from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    # app.config.update(
    #     MONGO_HOST='localhost',
    #     MONGO_PORT=27017,
    #     #MONGO_USERNAME='bjhee',
    #     #MONGO_PASSWORD='111111',
    #     MONGO_DBNAME='demo'
    # )

    app.config["MONGO_URI"] = "mongodb://localhost:27017/demo"
    mongo.init_app(app)

    from app.users.controller import mod as users_mod

    app.register_blueprint(users_mod)

    return app