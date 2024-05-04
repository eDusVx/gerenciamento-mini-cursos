from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .CoreModulle import UseCaseFactory

class CoreController:
    def __init__(self):
        self.registrarUsuarioUseCase = UseCaseFactory.create_registrar_usuario_use_case()

    @jwt_required()
    async def registrar_usuario(self):
        try:
            response = await self.registrarUsuarioUseCase.execute(request.json)
            
            return jsonify({'data': response}), 200
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @jwt_required()
    async def hello_world():
        try:
            return jsonify({'data': 'Hello World!'}), 200
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        

registrar_usuario_controller = Blueprint('registrar_usuario_controller', __name__)
registrar_usuario_controller.add_url_rule('/core/registrar-usuario', view_func=CoreController().registrar_usuario, methods=['POST'])

