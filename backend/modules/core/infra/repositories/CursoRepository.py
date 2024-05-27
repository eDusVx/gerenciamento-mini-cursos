from ...domain.Curso import Curso
from ...domain.repositories.CursoRepository import CursoRepositoryInteface
from dbconfig import Database
from ..mappers.CursoMapper import CursoMapper


class CursoRepositoryImpl(CursoRepositoryInteface):
    def __init__(self, cursoMapper: CursoMapper):
        self.cursoMapper = cursoMapper

    def save(self, curso: Curso):
        try:
            connection = Database.obter_conexao()
            cursor = connection.cursor()
            sql = "INSERT INTO curso (id, nome_curso, descricao, duracao, curso_relacionado, status_curso, quantidade_max_alunos) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (
                str(curso.id),
                curso.nome,
                curso.descricao,
                curso.cargaHoraria,
                curso.cursoRelacionado,
                curso.status,
                curso.numeroVagas
            )
            cursor.execute(sql, val)
            connection.commit()
            cursor.close()
            return f"Curso {curso.nome} salvo com sucesso!"
        except Exception as e:
            raise Exception(f"Erro ao salvar curso: {e}")
