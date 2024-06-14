from ...domain.Curso import Curso
from ...domain.repositories.CursoRepository import CursoRepositoryInteface
from dbconfig import Database
from ..mappers.CursoMapper import CursoMapper
from datetime import datetime
import os
import math


class CursoRepositoryImpl(CursoRepositoryInteface):
    def __init__(self, cursoMapper: CursoMapper):
        self.cursoMapper = cursoMapper

    def save(self, curso: Curso):
        try:
            connection = Database.obter_conexao()
            cursor = connection.cursor()
            sql = "INSERT INTO curso (id, nome_curso, descricao, duracao, curso_relacionado, status_curso, quantidade_max_alunos, data_inclusao, data_modificacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (
                str(curso.id),
                curso.nome,
                curso.descricao,
                curso.cargaHoraria,
                curso.cursoRelacionado,
                curso.status,
                curso.numeroVagas,
                curso.dataInclusao,
                datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
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
    
    def findAll(self, pagina: int):
        try:
            tamanho_pagina = int(os.getenv("TAMANHO_PAGINA"))
            cursos = []
            connection = Database.obter_conexao()
            cursor = connection.cursor(dictionary=True)
            offset = (pagina - 1) * tamanho_pagina
            sql = "SELECT * FROM curso order by data_inclusao ASC LIMIT %s OFFSET %s"
            cursor.execute(sql, (tamanho_pagina, offset))
            result = cursor.fetchall()
            if len(result) == 0:
                raise ValueError("Nenhum Curso cadastrado")
            for row in result:
                curso = self.cursoMapper.modelToDomain(row)
                cursos.append(curso)
            return cursos
        except Exception as e:
            raise Exception(f"Erro ao buscar cursos: {e}")

    
    def findByStatus(self, status: str, pagina: int):
        try:
            tamanho_pagina = int(os.getenv("TAMANHO_PAGINA"))
            cursos = []
            connection = Database.obter_conexao()
            cursor = connection.cursor(dictionary=True)
            offset = (pagina - 1) * tamanho_pagina
            sql = "SELECT * FROM curso WHERE status_curso = %s order by data_inclusao ASC LIMIT %s OFFSET %s"
            cursor.execute(sql, (status, tamanho_pagina, offset))
            result = cursor.fetchall()
            if len(result) == 0:
                raise ValueError("Nenhum Curso cadastrado")
            for row in result:
                curso = self.cursoMapper.modelToDomain(row)
                cursos.append(curso)
            return cursos
        except Exception as e:
            raise Exception(f"Erro ao buscar cursos: {e}")
    
    def findPagesNumber(self):
        try:
            connection = Database.obter_conexao()
            cursor = connection.cursor()
            tamanho_pagina = int(os.getenv("TAMANHO_PAGINA"))

            if tamanho_pagina <= 0:
                raise ValueError("TAMANHO_PAGINA must be a positive integer")

            sql = "SELECT count(*) FROM curso"
            cursor.execute(sql)
            result = cursor.fetchone()

            if result is None or len(result) == 0:
                raise ValueError("Failed to fetch count from the database")

            paginas = math.ceil(result[0] / tamanho_pagina)
            return paginas
        except Exception as e:
            raise Exception(f"Erro ao buscar número de páginas: {e}")

    

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
    
    def remove(self, cursoId: str):
        try:
            connection = Database.obter_conexao()
            cursor = connection.cursor()
            sql = "DELETE FROM curso WHERE id = %s"
            val = (cursoId,)
            print(sql)
            cursor.execute(sql, val)
            connection.commit()

        except Exception as e:
            raise Exception(f"Erro ao deletar curso: {e}")
    