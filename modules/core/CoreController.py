from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .CoreModulle import UseCaseFactory

class CoreController:
    def __init__(self):
        self.buscarCategoriasQuery = UseCaseFactory.create_buscar_categorias_query()

    @jwt_required()     
    async def buscarCategorias(self):
        try:
            response = await self.buscarCategoriasQuery.execute()
            
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
        

coreController = Blueprint('coreController', __name__)
coreController.add_url_rule('/core/buscar-categorias', view_func=CoreController().buscarCategoriasQuery, methods=['POST'])

