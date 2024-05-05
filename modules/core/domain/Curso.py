import uuid

class Curso:
    def __init__(self, nome: str, descricao: str, cargaHoraria: int, localizacao: str, professor: list, numeroVagas: int, notas: Notas, categorias: Categorias, alunos: int):
        self.id = uuid.uuid4()
        self.nome = nome
        self.descricao = descricao
        self.cargaHoraria = cargaHoraria
        self.localizacao = localizacao
        self.professor = professor
        self.numeroVagas = numeroVagas
        self.inscritos = [] 
        self.notas = notas
        self.categorias = categorias
        self.alunos = alunos

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def cargaHoraria(self):
        return self.__cargaHoraria

    @property
    def localizacao(self):
        return self.__localizacao

    @property
    def professor(self):
        return self.__professor

    @property
    def numeroVagas(self):
        return self.__numeroVagas

    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError('Nome do curso não informado!')
        self.__nome = nome

    @descricao.setter
    def descricao(self, descricao):
        if not descricao:
            raise ValueError('Descrição do curso não informada!')
        self.__descricao = descricao

    @cargaHoraria.setter
    def cargaHoraria(self, cargaHoraria):
        if not cargaHoraria or not isinstance(cargaHoraria, int):
            raise ValueError('Horários inválidos!')
        self.__cargaHoraria = cargaHoraria

    @localizacao.setter
    def localizacao(self, localizacao):
        if not localizacao:
            raise ValueError('Localização não informada!')
        self.__localizacao = localizacao

    @professor.setter
    def professor(self, professor):
        if not professor or not isinstance(professor, list):
            raise ValueError('Lista de professor inválida!')
        self.__professor = professor

    @numeroVagas.setter
    def numeroVagas(self, numeroVagas):
        if not isinstance(numeroVagas, int) or numeroVagas <= 0:
            raise ValueError('Número de vagas inválido!')
        self.__numeroVagas = numeroVagas


    @staticmethod
    def create(nome: str, descricao: str, cargaHoraria: list, localizacao: str, professor: list, numeroVagas: int):
        return Curso(nome, descricao, cargaHoraria, localizacao, professor, numeroVagas)
