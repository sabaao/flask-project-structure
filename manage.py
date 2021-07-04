from flask_script import Manager
from flask import Flask

app = Flask(__name__)

# setting app
manager = Manager(app)

# define command
@manager.command
def hello():
    """Print Hello"""
    print("Hello")

if __name__=="__main__":
    manager.run()