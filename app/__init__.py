from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.users.controller import mod as users_mod

    app.register_blueprint(users_mod)

    return app