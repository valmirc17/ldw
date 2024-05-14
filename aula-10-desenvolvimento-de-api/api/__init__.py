from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow

app = Flask(__name__)
api = Api(app)

# Definindo conexão com o banco antes de instanciar o mongo
app.config['MONGO_URI'] = 'mongodb://localhost:27017/apigames'
mongo = PyMongo(app)
ma = Marshmallow(app)

from .views import games_views