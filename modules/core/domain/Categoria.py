import uuid

class Categoria:
    def __init__(self, nome: str):
        self.id = uuid.uuid4()
        self.nome = nome
        self.aulas = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError('Nome da categoria não informado!')
        self.__nome = nome

    def adicionar_aula(self, aula):
        self.aulas.append(aula)

    def remover_aula(self, aula):
        if aula in self.aulas:
            self.aulas.remove(aula)

    def listar_aulas(self):
        return self.aulas

    @staticmethod
    def create(nome: str):
        return Categoria(nome)
