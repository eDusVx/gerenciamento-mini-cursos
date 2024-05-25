class Nota:
    def __init__(self, prova: int, alunoId: str, valor: float):
        self.prova = prova
        self.alunoId = alunoId
        self.valor = valor

    @property
    def prova(self):
        return self.__prova

    @property
    def alunoId(self):
        return self.__alunoId

    @property
    def valor(self):
        return self.__valor

    @prova.setter
    def prova(self, prova):
        if not isinstance(prova, int) or prova <= 0:
            raise ValueError("Número da prova inválido!")
        self.__prova = prova

    @alunoId.setter
    def alunoId(self, alunoId):
        if not alunoId:
            raise ValueError("ID do aluno não informado!")
        self.__alunoId = alunoId

    @valor.setter
    def valor(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("Valor da nota inválido!")
        self.__valor = valor

    @staticmethod
    def create(prova: int, alunoId: str, valor: float):
        return Nota(prova, alunoId, valor)
