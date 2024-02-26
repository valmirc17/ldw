# Importando o Flask na aplicação
from flask import Flask

# Carregando o Flask na variável app
app = Flask(__name__)

# Definindo a rota principal
@app.route('/')
def home():
    # Retorno que será exibido na rota
    return '<h1>Essa é a homepage!</h1>'

@app.route('/games')
def games():
    return '<h1>Bem-vindo a página de games!</h1>'        

# Se for executado diretamente pelo interpretador (arquivo principal)
if __name__=='__main__':
    # Rodando a aplicação no localhost, porta 5000, modo debug ativado
    app.run(host='localhost', port=5000, debug=True)