from flask import Flask
import os

app = Flask(__name__)

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "GoMount1808!"

app.config.from_object(Config)

from app import routes
