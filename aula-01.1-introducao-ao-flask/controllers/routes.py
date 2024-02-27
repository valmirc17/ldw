from flask import render_template

def init_app(app):
    # Definindo a rota principal
    @app.route('/')
    def home():
        # Retorno que será exibido na rota
        return render_template('index.html')

    @app.route('/games')
    def games():
        game = {
            'Título' : 'CS-GO',
            'Ano': 2012,
            'Categoria' : 'FPS Online'
        }
        jogadores = [
            'Fabio',
            'Ryan',
            'PedrinhoMotoBoy',
            'Ricardo'
        ]
        return render_template('games.html',game=game,jogadores=jogadores)       
