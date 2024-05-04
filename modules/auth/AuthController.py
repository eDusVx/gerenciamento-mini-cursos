from flask import Blueprint, request, jsonify
from .AuthModulle import UseCaseFactory

class AuthController:
    def __init__(self):
        self.efetuarLoginUsuarioUseCase = UseCaseFactory.create_efetuar_login_usuario_use_case()

    async def efetuarLoginUsuario(self):
        try:
            data = request.json
            email = data.get('email')
            senha = data.get('senha')

            response = await self.efetuarLoginUsuarioUseCase.execute(email, senha)
            
            return jsonify({'data': response}), 200
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500

auth_controller = Blueprint('auth_controller', 'AuthController')
auth_controller.add_url_rule('/auth/login', view_func=AuthController().efetuarLoginUsuario, methods=['POST'])


