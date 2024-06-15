import uuid
from typing import Optional
from datetime import datetime

class Aula:
    def __init__(self, nome: str, descricao: str, conteudo: str, duracao: int, id: Optional[uuid.UUID] = None, dataInclusao: Optional[datetime] = None,):
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id
        self.nome = nome
        self.descricao = descricao
        self.conteudo = conteudo
        self.duracao = duracao
        self.dataInclusao = dataInclusao
        

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError("Nome da aula não informado!")
        self.__nome = nome
    
    @property
    def dataInclusao(self):
        return self.__dataInclusao
        
    @dataInclusao.setter
    def dataInclusao(self, dataInclusao: Optional[datetime]):
        if dataInclusao is None:
            self.__dataInclusao = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        else:
            self.__dataInclusao = dataInclusao

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if not descricao:
            raise ValueError("Descrição da aula não informada!")
        self.__descricao = descricao

    @property
    def conteudo(self):
        return self.__conteudo

    @conteudo.setter
    def conteudo(self, conteudo):
        if not conteudo:
            raise ValueError("Conteúdo da aula não informado!")
        self.__conteudo = conteudo

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao):
        if not duracao:
            raise ValueError("Duração da aula não informada!")
        self.__duracao = duracao

    @staticmethod
    def create(nome: str, descricao: str, conteudo: str, duracao: int):
        return Aula(nome, descricao, conteudo, duracao)

    @staticmethod
    def carregar(
        id: uuid.UUID,
        nome: str,
        descricao: str,
        conteudo: str,
        duracao: int,
        dataInclusao: datetime
    ):
        return Aula(
            nome,
            descricao,
            conteudo,
            duracao,
            id,
            dataInclusao=dataInclusao
        )

    def toDto(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "conteudo": self.conteudo,
            "duracao": self.duracao,
            "dataInclsuao": str(self.dataInclusao)
        }
    