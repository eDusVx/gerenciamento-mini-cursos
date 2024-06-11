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

    def find(self, cursoId: str):
        try:
            connection = Database.obter_conexao()
            cursor = connection.cursor(dictionary=True)
            sql = "SELECT*FROM curso WHERE id = %s"
            val = (cursoId,)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            print(result)
            if result:
                curso = self.cursoMapper.modelToDomain(result)
                return curso
            else:
                raise ValueError(
                    f"Nenhum Curso cadastrado para o id {cursoId}"
                )
        except Exception as e:
            raise Exception(f"Erro ao buscar usuário: {e}")
    

    def update(self, curso: Curso):
        try:
            connection = Database.obter_conexao()
            cursor = connection.cursor()

            fields_to_update = []
            values = []

            if curso.nome:
                fields_to_update.append("nome_curso = %s")
                values.append(curso.nome)
            if curso.descricao:
                fields_to_update.append("descricao = %s")
                values.append(curso.descricao)
            if curso.cargaHoraria:
                fields_to_update.append("duracao = %s")
                values.append(curso.cargaHoraria)
            if curso.cursoRelacionado:
                fields_to_update.append("curso_relacionado = %s")
                values.append(curso.cursoRelacionado)
            if curso.numeroVagas:
                fields_to_update.append("quantidade_max_alunos = %s")
                values.append(curso.numeroVagas)
            if curso.cargaHoraria:
                fields_to_update.append("duracao = %s")
                values.append(curso.cargaHoraria)

            if not fields_to_update:
                raise ValueError("Nenhum campo para atualizar foi fornecido")

            values.append(str(curso.id))
            sql = f"UPDATE curso SET {', '.join(fields_to_update)} WHERE id = %s"
            cursor.execute(sql, values)
            connection.commit()
        except Exception as e:
            raise Exception(f"Erro ao atualizar curso: {e}")