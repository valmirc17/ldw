from api import PyMongo

class Game():
    def __init__(self, titulo, descricao, ano):
        self.titulo = titulo
        self.descricao = descricao
        self.ano = ano