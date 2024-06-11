from ...domain.Curso import Curso
import uuid


# TODO Implementar relacão cursos alunos e professores e importar no mapper
class CursoMapper:
    def modelToDomain(self, cursoModel: dict):
        curso = Curso.carregar(
            id=uuid.UUID(cursoModel["id"]),
            nome=cursoModel["nome_curso"],
            descricao=cursoModel["descricao"],
            cargaHoraria=cursoModel["duracao"],
            professor="05585299174",
            numeroVagas=cursoModel["quantidade_max_alunos"],
            cursoRelacionado=cursoModel["curso_relacionado"],
            status=cursoModel["status_curso"],
            alunos=None,
            aula=None
        )
        return curso

