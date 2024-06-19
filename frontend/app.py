from flask import Flask, render_template
from dotenv import load_dotenv
import os
from middlewares.authMiddleware import authMiddleware

from blueprints.auth.routes import auth_bp
from blueprints.user.routes import user_bp
from blueprints.course.routes import course_bp

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
app.config['API_URL'] = os.getenv('API_URL')

# Middleware para adicionar o token de autenticação às requisições
app.before_request(authMiddleware)

# Blueprints das rotas dos services
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(course_bp, url_prefix='/course')

@app.route('/login')
def login():
    api_url = app.config['API_URL']
    return render_template('login.html', api_url=api_url)

if __name__ == '__main__':
    app.run(debug=True)