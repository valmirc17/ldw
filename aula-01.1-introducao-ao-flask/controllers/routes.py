from flask import render_template, request

jogadores = []
jogos = []
gamelist = [{
            'Titulo' : 'CS-GO',
            'Ano': 2012,
            'Categoria' : 'FPS Online'
        }]

def init_app(app):
    # Definindo a rota principal
    @app.route('/')
    def home():
        # Retorno que será exibido na rota
        return render_template('index.html')
    
    @app.route('/games',methods=['GET','POST'])
    def games():
        game = gamelist[0]
        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))
            if request.form.get('jogo'):
                jogos.append(request.form.get('jogo'))
        return render_template('games.html',game=game,jogadores=jogadores,jogos=jogos)
           
    @app.route('/cadgames',methods=['GET','POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('Titulo') and request.form.get('Ano') and request.form.get('Categoria'):
                gamelist.append({'Titulo':request.form.get('Titulo'),'Ano':request.form.get('Ano'),'Categoria':request.form.get('Categoria')})
        return render_template('cadgames.html',gamelist=gamelist)