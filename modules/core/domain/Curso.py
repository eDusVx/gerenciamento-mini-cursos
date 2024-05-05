import uuid
from .SubCategoria import SubCategoria
from .Notas import Nota
from enum import Enum

class Categoria(Enum):
    TECNOLOGIA_DA_INFORMACAO = 'TECNOLOGIA DA FORMACAO'
    MARKETING_DIGITAL = 'MARKETING DIGITAL'
    DESIGN = 'DESIGN'
    FINANCAS = 'FINANCAS'

class Curso:
    def __init__(self, nome: str, descricao: str, cargaHoraria: int, localizacao: str, professor: list, numeroVagas: int, notas: Nota, subCategoria: SubCategoria, alunos: int, categoria: Categoria):
        self.id = uuid.uuid4()
        self.nome = nome
        self.descricao = descricao
        self.cargaHoraria = cargaHoraria
        self.localizacao = localizacao
        self.professor = professor
        self.numeroVagas = numeroVagas
        self.inscritos = [] 
        self.notas = notas
        self.subCategoria = subCategoria
        self.alunos = alunos
        self.categoria = categoria

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
    
    @property
    def categoria(self):
        return self.__categoria

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
    
    @categoria.setter
    def categoria(self, categoria):
        if not categoria:
            raise ValueError('Categoria não informada!')
        if not isinstance(categoria, Categoria):
            raise ValueError('Categoria inválida!')
        self.__categoria = categoria


    @staticmethod
    def create(nome: str, descricao: str, cargaHoraria: list, localizacao: str, professor: list, numeroVagas: int, categoria: Categoria):
        return Curso(nome, descricao, cargaHoraria, localizacao, professor, numeroVagas, categoria)
