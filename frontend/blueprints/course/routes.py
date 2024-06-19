from flask import Blueprint, request, jsonify, current_app
from services.course_service import CourseService

course_bp = Blueprint('course', __name__)

course_service = CourseService(api_url=current_app.config['API_URL'])

@course_bp.route('/registrar-curso', methods=['POST'])
def registrar_curso():
    data = request.json
    response = course_service.registrar_curso(data)
    return jsonify(response)

@course_bp.route('/remover-curso', methods=['DELETE'])
def remover_curso():
    data = request.json
    response = course_service.remover_curso(data["id"])
    return jsonify(response)

@course_bp.route('/remover-aluno-curso', methods=['DELETE'])
def remover_aluno_curso():
    data = request.json
    response = course_service.remover_aluno_curso(data["ra"], data["cursoId"])
    return jsonify(response)

@course_bp.route('/remover-aula-curso', methods=['DELETE'])
def remover_aula_curso():
    data = request.json
    response = course_service.remover_aula_curso(data["cursoId"], data["professorId"], data["aulaId"])
    return jsonify(response)

@course_bp.route('/cadastrar-aula-curso', methods=['POST'])
def cadastrar_aula_curso():
    data = request.json
    response = course_service.cadastrar_aula_curso(data)
    return jsonify(response)

@course_bp.route('/atualizar-curso', methods=['PUT'])
def atualizar_curso():
    data = request.json
    response = course_service.atualizar_curso(data)
    return jsonify(response)

@course_bp.route('/buscar-cursos', methods=['GET'])
def buscar_cursos():
    pagina = request.args.get('pagina', 1)
    response = course_service.buscar_cursos(pagina)
    return jsonify(response)


@course_bp.route('/inscrever-aluno-curso', methods=['POST'])
def inscrever_aluno_curso():
    data = request.json
    response = course_service.inscrever_aluno_curso(data["ra"], data["cursoId"])
    return jsonify(response)
