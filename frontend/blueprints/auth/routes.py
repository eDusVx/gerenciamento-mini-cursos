from flask import Blueprint, request, jsonify, current_app
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.before_app_request
def before_request():
    if not hasattr(current_app, 'auth_service'):
        current_app.auth_service = AuthService(api_url=current_app.config['API_URL'])

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    response = current_app.auth_service.login(data["email"], data["senha"])

    # Salvar token no session storage
    if response["status"] == 200:
        token = response["data"]["token"]
        response["data"]["token"] = token

    return jsonify(response)

@auth_bp.route('/registrar-usuario', methods=['POST'])
def registrar_usuario():
    data = request.json
    response = current_app.auth_service.registrar_usuario(data)
    return jsonify(response)
