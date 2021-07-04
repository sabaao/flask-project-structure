from flask_script import Manager
from flask import Flask
from app import create_app

# setting app
app = create_app()
manager = Manager(app)

# define command
@manager.command
def hello():
    """Print Hello"""
    print("Hello")

if __name__=="__main__":
    manager.run()