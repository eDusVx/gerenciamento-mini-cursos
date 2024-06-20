from flask import Flask, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import os

from middlewares.unauthorizedMiddleware import unauthorizedMiddleware

from flask_bootstrap import Bootstrap

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
app.config['API_URL'] = os.getenv('API_URL')

# Middlewares
app.after_request(unauthorizedMiddleware)

Bootstrap(app)

@app.route('/')
def login():
    api_url = app.config['API_URL']
    return render_template('login.html', api_url=api_url)

@app.route('/home')
def home():
    return render_template('home.html', jwt_secret=os.getenv('JWT_SECRET'))

@app.route('/cursos')
def cursos():
    api_url = app.config['API_URL']
    return render_template('cursos.html', api_url=api_url, jwt_secret=os.getenv('JWT_SECRET'))

@app.route('/adicionar_curso')
def adicionar_curso():
    api_url = app.config['API_URL']
    return render_template('adicionar_curso.html', api_url=api_url, jwt_secret=os.getenv('JWT_SECRET'))

@app.route('/cursos/editar/<string:id>')
def editar_curso(id):
    api_url = app.config['API_URL']
    return render_template('editar_curso.html', api_url=api_url, id=id, jwt_secret=os.getenv('JWT_SECRET'))

if __name__ == '__main__':
    app.run(debug=True, port=4200)