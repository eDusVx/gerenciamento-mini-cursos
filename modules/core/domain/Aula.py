import uuid


class Aula:
    def __init__(self, data: str, horario: str, conteudo: str, presenca: int):
        self.id = uuid.uuid4()
        self.data = data
        self.horario = horario
        self.conteudo = conteudo
        self.presenca = presenca

    @property
    def data(self):
        return self.__data

    @property
    def horario(self):
        return self.__horario

    @property
    def conteudo(self):
        return self.__conteudo

    @data.setter
    def data(self, data):
        if not data:
            raise ValueError('Data não informada!')
        self.__data = data

    @horario.setter
    def horario(self, horario):
        if not horario:
            raise ValueError('Horário não informado!')
        self.__horario = horario

    @conteudo.setter
    def conteudo(self, conteudo):
        if not conteudo:
            raise ValueError('Conteúdo não informado!')
        self.__conteudo = conteudo

    @staticmethod
    def create( data: str, horario: str, conteudo: str):
        return Aula(data, horario, conteudo)