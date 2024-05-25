import uuid
from .Aula import Aula
from typing import List


class SubCategoria:
    def __init__(self, nome: str, aula: List[Aula]):
        self.id = uuid.uuid4()
        self.nome = nome
        self.aulas = aula

    @property
    def nome(self):
        return self.__nome

    @property
    def aulas(self):
        return self.aulas

    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError("Nome da SubCategoria não informado!")
        self.__nome = nome

    def adicionar_aula(self, aula):
        if not aula:
            raise ValueError("Aula inválida ou não informada!")
        self.aulas.append(aula)

    def remover_aula(self, aula):
        if not aula:
            raise ValueError("Aula inválida ou não informada!")
        if aula in self.aulas:
            self.aulas.remove(aula)

    @staticmethod
    def create(nome: str, aula: List[Aula]):
        return SubCategoria(nome, aula)
