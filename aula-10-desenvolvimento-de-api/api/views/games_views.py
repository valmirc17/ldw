from flask_restful import Resource
from api import api
from ..schemas import game_schema
from ..models import game_model
from ..services import game_service
from flask import make_response, jsonify

class GameList(Resource):
    def get(self):
        games = game_service.get_games()
        g = game_schema.GameSchema(many=True)
        return 

#class RecursosAPI(Resource):
#    def get(self):
#        return "Requisição GET - Responsável por recuperar informações da API."
#    def post(self):
#        return "Requisição POST - Responsável por criar novos recursos na API."
#    def put(self):
#        return "Requisição PUT - Responsável por alterar recursos na API."
#    def delete(self):
#       return "Requisição DELETE - Responsável por excluir recursos na API."
api.add_resource(GameList, '/games')
