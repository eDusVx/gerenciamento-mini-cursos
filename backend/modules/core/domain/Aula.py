import uuid
from datetime import date

class Aula:
    def __init__(self, nome: str, descricao: str, conteudo: str, duracao: date):
        self.id = uuid.uuid4()
        self.nome = nome
        self.descricao = descricao
        self.conteudo = conteudo
        self.duracao = duracao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError("Nome da aula não informado!")
        self.__nome = nome

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
        if not isinstance(duracao, date):
            raise ValueError("Duração deve ser uma data!")
        self.__duracao = duracao

    @staticmethod
    def create(nome: str, descricao: str, conteudo: str, duracao: date):
        return Aula(nome, descricao, conteudo, duracao)
