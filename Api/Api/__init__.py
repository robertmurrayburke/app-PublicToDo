from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask.ext.restless import APIManager
from flask.ext.cors import CORS

#enableing cors
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','postgresql+psycopg2:///todo')
db = SQLAlchemy(app)

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean)
    country = db.Column(db.Text)

db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(ToDo, methods=['GET', 'POST', 'DELETE', 'PUT'], collection_name='todo')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

import Api.views
