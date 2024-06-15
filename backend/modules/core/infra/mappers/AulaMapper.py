from ...domain.Aula import Aula
from datetime import datetime


class AulaMapper:
    def modelToDomain(self, aulaModel: dict):
        aula = Aula.carregar(
            nome = aulaModel["nome_aula"],
            descricao = aulaModel["descricao_aula"],
            conteudo = aulaModel["conteudo_aula"],
            duracao = aulaModel["duracao_aula"],
            id = aulaModel["id"],
            dataInclusao=datetime.strptime(str(aulaModel["data_inclusao"]), '%Y-%m-%d %H:%M:%S.%f')
        )
        return aula

