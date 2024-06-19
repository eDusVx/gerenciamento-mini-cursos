from flask import Blueprint, request, jsonify, current_app
from services.user_service import UserService

core_bp = Blueprint('core', __name__)

user_service = UserService(api_url=current_app.config['API_URL'])


@core_bp.route('/remover-usuario', methods=['DELETE'])
def remover_usuario():
    data = request.json
    response = user_service.remover_usuario(data["ra"])
    return jsonify(response)

@core_bp.route('/atualizar-usuario', methods=['PUT'])
def atualizar_usuario():
    data = request.json
    response = user_service.atualizar_usuario(data)
    return jsonify(response)

@core_bp.route('/buscar-usuarios', methods=['GET'])
def buscar_usuarios():
    pagina = request.args.get('pagina', 1)
    tipo_acesso = request.args.get('tipoAcesso', 'USER')
    response = user_service.buscar_usuarios(pagina, tipo_acesso)
    return jsonify(response)
