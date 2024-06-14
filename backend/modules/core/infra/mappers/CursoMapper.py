from ...domain.Curso import Curso
from .AulaMapper import AulaMapper
import uuid

class CursoMapper:
    def __init__(self, aulaMapper: AulaMapper):
        self.aulaMapper = aulaMapper

    def modelToDomain(self, cursoModel: dict):
        aulas = []
        for aula in cursoModel["aulas"]:
            aulas.append(self.aulaMapper.modelToDomain(aula))
        curso = Curso.carregar(
            id=uuid.UUID(cursoModel["id"]),
            nome=cursoModel["nome_curso"],
            descricao=cursoModel["descricao"],
            cargaHoraria=cursoModel["duracao"],
            professor="05585299174",
            numeroVagas=cursoModel["quantidade_max_alunos"],
            cursoRelacionado=cursoModel["curso_relacionado"],
            status=cursoModel["status_curso"],
            alunos=cursoModel["alunos"],
            aula=aulas
        )
        return curso

