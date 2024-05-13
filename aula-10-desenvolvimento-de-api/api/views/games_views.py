from flask_restful import Resource
from api import api

class GameList(Resource):
    def get(self):
        return "Olá mundo! API rodando..."

class RecursosAPI(Resource):
    def get(self):
        return "Requisição GET - Responsável por recuperar informações da API."
    def post(self):
        return "Requisição POST - Responsável por criar novos recursos na API."
    def put(self):
        return "Requisição PUT - Responsável por alterar recursos na API."
    def delete(self):
        return "Requisição DELETE - Responsável por excluir recursos na API."
api.add_resource(GameList, '/games')
api.add_resource(RecursosAPI, '/recursos')