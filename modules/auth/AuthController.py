from flask import Blueprint, request, jsonify
from .AuthModulle import UseCaseFactory
from flask_jwt_extended import jwt_required


class AuthController:
    def __init__(self):
        self.efetuarLoginUsuarioUseCase = (
            UseCaseFactory.create_efetuar_login_usuario_use_case()
        )
        self.registrarUsuarioUseCase = (
            UseCaseFactory.create_registrar_usuario_use_case()
        )

    async def efetuarLoginUsuario(self):
        try:
            data = request.json
            email = data.get("email")
            senha = data.get("senha")

            response = await self.efetuarLoginUsuarioUseCase.execute(email, senha)

            return jsonify({"data": response}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    async def registrar_usuario(self):
        try:
            response = await self.registrarUsuarioUseCase.execute(request.json)

            return jsonify({"data": response}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500


auth_controller = Blueprint("auth_controller", "AuthController")
auth_controller.add_url_rule(
    "/auth/login", view_func=AuthController().efetuarLoginUsuario, methods=["POST"]
)
auth_controller.add_url_rule(
    "/auth/registrar-usuario",
    view_func=AuthController().registrar_usuario,
    methods=["POST"],
)
