from ...domain.Aula import Aula
import uuid


class AulaMapper:
    def modelToDomain(self, aulaModel: dict):
        aula = Aula.carregar(
            nome = aulaModel["nome_aula"],
            descricao = aulaModel["descricao_aula"],
            conteudo = aulaModel["conteudo_aula"],
            duracao = aulaModel["duracao_aula"],
            id = aulaModel["id"]
        )
        return aula

