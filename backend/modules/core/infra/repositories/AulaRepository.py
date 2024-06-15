from ...domain.Aula import Aula
from ...domain.repositories.AulaRepository import AulaRepositoryInterface
from dbconfig import Database
from datetime import datetime
from typing import List

class AulaRepositoryImpl(AulaRepositoryInterface):
    def saveList(self, aulas: List[Aula], cursoId: str):
        try:
            connection = Database.obter_conexao()
            cursor = connection.cursor()
            sql = """INSERT IGNORE INTO aulas (id, nome_aula, descricao_aula, conteudo_aula, id_curso, data_inclusao, data_modificacao, duracao_aula)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            for aula in aulas:
                val = (
                    str(aula.id),
                    aula.nome,
                    aula.descricao,
                    aula.conteudo,
                    str(cursoId),
                    aula.dataInclusao,
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),
                    aula.duracao
                )
                cursor.execute(sql, val)
            connection.commit()
            cursor.close()
            return f"aulas salvas com sucesso!"
        except Exception as e:
            raise Exception(f"Erro ao salvar aulas: {e}")
