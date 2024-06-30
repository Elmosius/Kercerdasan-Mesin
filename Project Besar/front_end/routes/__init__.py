from flask import Flask
import os

from routes.home import home

base_dir = os.path.abspath(os.path.dirname(__file__))
templates = os.path.join(base_dir, '..', 'templates')
static = os.path.join(base_dir, '..', 'static')
app = Flask(__name__, template_folder=templates,static_folder=static)  
app.register_blueprint(home)