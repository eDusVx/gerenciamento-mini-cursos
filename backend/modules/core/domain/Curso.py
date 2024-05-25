import uuid
from .SubCategoria import SubCategoria
from .Notas import Nota
from enum import Enum
from typing import List


class Categoria(Enum):
    TECNOLOGIA_DA_INFORMACAO = "TECNOLOGIA DA INFORMACAO"
    MARKETING_DIGITAL = "MARKETING DIGITAL"
    DESIGN = "DESIGN"
    FINANCAS = "FINANCAS"


class Curso:
    def __init__(
        self,
        nome: str,
        descricao: str,
        cargaHoraria: int,
        professorId: str,
        numeroVagas: int,
        notas: Nota,
        subCategoria: List[SubCategoria],
        alunosId: List[str],
        categoria: Categoria,
    ):
        self.id = uuid.uuid4()
        self.nome = nome
        self.descricao = descricao
        self.cargaHoraria = cargaHoraria
        self.professorId = professorId
        self.numeroVagas = numeroVagas
        self.notas = notas
        self.subCategoria = subCategoria
        self.alunosId = alunosId
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
    def professorId(self):
        return self.__professorId

    @property
    def numeroVagas(self):
        return self.__numeroVagas

    @property
    def categoria(self):
        return self.__categoria

    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError("Nome do curso não informado!")
        self.__nome = nome

    @descricao.setter
    def descricao(self, descricao):
        if not descricao:
            raise ValueError("Descrição do curso não informada!")
        self.__descricao = descricao

    @cargaHoraria.setter
    def cargaHoraria(self, cargaHoraria):
        if not cargaHoraria:
            raise ValueError("Carga horária não informada!")
        if not isinstance(cargaHoraria, int):
            raise ValueError("Horários inválidos!")
        self.__cargaHoraria = cargaHoraria

    @professorId.setter
    def professorId(self, professorId):
        if not professorId or not isinstance(professorId, str):
            raise ValueError("Lista de professorId inválida!")
        self.__professorId = professorId

    @numeroVagas.setter
    def numeroVagas(self, numeroVagas):
        if not isinstance(numeroVagas, int) or numeroVagas <= 0:
            raise ValueError("Número de vagas inválido!")
        self.__numeroVagas = numeroVagas

    @categoria.setter
    def categoria(self, categoria):
        if not categoria:
            raise ValueError("Categoria não informada!")
        if not isinstance(categoria, Categoria):
            raise ValueError("Categoria inválida!")
        self.__categoria = categoria

    @staticmethod
    def create(
        nome: str,
        descricao: str,
        cargaHoraria: int,
        professorId: str,
        numeroVagas: int,
        categoria: Categoria,
        notas=None,
        subCategoria=None,
        alunosId=None,
    ):
        return Curso(
            nome,
            descricao,
            cargaHoraria,
            professorId,
            numeroVagas,
            notas,
            subCategoria,
            alunosId,
            categoria,
        )

    def toDto(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "cargaHoraria": self.cargaHoraria,
            "professorId": self.professorId,
            "numeroVagas": self.numeroVagas,
            "notas": self.notas,
            "subCategoria": self.subCategoria,
            "alunosId": self.alunosId,
            "categoria": self.categoria.value,
        }
