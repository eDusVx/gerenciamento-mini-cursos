from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from .CoreModulle import UseCaseFactory


class CoreController:
    def __init__(self):
        self.registrarCursoUseCase = UseCaseFactory.createRegistrarCursoUseCase()
        self.removerUsuarioUseCase = UseCaseFactory.createRemoverUsuarioUseCase()

    @jwt_required()
    async def registrarCurso(self):
        try:
            response = await self.registrarCursoUseCase.execute(request.json)

            return jsonify({"data": response}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @jwt_required()
    async def removerUsuario(self):
        try:
            request.json['tipoAcesso'] = get_jwt()["tipoAcesso"]

            response = await self.removerUsuarioUseCase.execute(request.json)

            return jsonify({"data": response}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @jwt_required()
    async def hello_world(self):
        try:
            return jsonify({"data": "Hello World!"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500


coreController = Blueprint("coreController", __name__)

coreController.add_url_rule(
    "/core/registrar-curso",
    view_func=CoreController().registrarCurso,
    methods=["POST"],
)
coreController.add_url_rule(
    "/core/remover-usuario",
    view_func=CoreController().removerUsuario,
    methods=["DELETE"],
)
coreController.add_url_rule(
    "/core/hello",
    view_func=CoreController().hello_world,
    methods=["GET"],
)
