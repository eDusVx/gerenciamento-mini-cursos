from flask import Blueprint, request, jsonify, current_app
from services.user_service import UserService

user_bp = Blueprint('user', __name__)

@user_bp.before_app_request
def before_request():
    if not hasattr(current_app, 'user_service'):
        current_app.user_service = UserService(api_url=current_app.config['API_URL'])

@user_bp.route('/remover-usuario', methods=['DELETE'])
def remover_usuario():
    data = request.json
    response = current_app.user_service.remover_usuario(data["ra"])
    return jsonify(response)

@user_bp.route('/atualizar-usuario', methods=['PUT'])
def atualizar_usuario():
    data = request.json
    response = current_app.user_service.atualizar_usuario(data)
    return jsonify(response)

@user_bp.route('/buscar-usuarios', methods=['GET'])
def buscar_usuarios():
    pagina = request.args.get('pagina', 1)
    tipo_acesso = request.args.get('tipoAcesso', 'USER')
    response = current_app.user_service.buscar_usuarios(pagina, tipo_acesso)
    return jsonify(response)
