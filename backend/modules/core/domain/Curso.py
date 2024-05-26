import uuid
from typing import List, Optional
from .Aula import Aula

class Curso:
    def __init__(
        self,
        nome: str,
        descricao: str,
        cargaHoraria: int,
        professor: str,
        numeroVagas: int,
        cursoRelacionado: str,
        status: str,
        alunos: Optional[List[str]] = None,
        aula: Optional[List[Aula]] = None
    ):
        self.id = uuid.uuid4()
        self.nome = nome
        self.descricao = descricao
        self.cargaHoraria = cargaHoraria
        self.professor = professor
        self.numeroVagas = numeroVagas
        self.cursoRelacionado = cursoRelacionado
        self.status = status
        self.alunos = alunos
        self.aula = aula

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError("Nome do curso não informado!")
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if not descricao:
            raise ValueError("Descrição do curso não informada!")
        self.__descricao = descricao

    @property
    def cargaHoraria(self):
        return self.__cargaHoraria

    @cargaHoraria.setter
    def cargaHoraria(self, cargaHoraria):
        if not cargaHoraria:
            raise ValueError("Carga horária não informada!")
        if not isinstance(cargaHoraria, int):
            raise ValueError("Horários inválidos!")
        self.__cargaHoraria = cargaHoraria

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, professor):
        if not professor or not isinstance(professor, str):
            raise ValueError("Lista de professorId inválida!")
        self.__professor = professor

    @property
    def numeroVagas(self):
        return self.__numeroVagas

    @numeroVagas.setter
    def numeroVagas(self, numeroVagas):
        if not isinstance(numeroVagas, int) or numeroVagas <= 0:
            raise ValueError("Número de vagas inválido!")
        self.__numeroVagas = numeroVagas

    @property
    def cursoRelacionado(self):
        return self.__cursoRelacionado

    @cursoRelacionado.setter
    def cursoRelacionado(self, cursoRelacionado):
        if not cursoRelacionado:
            raise ValueError("CursoRelacionado não informado!")
        self.__cursoRelacionado = cursoRelacionado

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if not status:
            raise ValueError("Status não informado!")
        self.__status = status

    @property
    def alunos(self):
        return self.__alunos

    @alunos.setter
    def alunos(self, alunos):
        if alunos is not None and len(alunos) == 0:
            raise ValueError("Alunos não informados!")
        self.__alunos = alunos

    @property
    def aula(self):
        return self.__aula

    @aula.setter
    def aula(self, aula):
        if aula is not None and len(aula) == 0:
            raise ValueError("Aulas não informadas!")
        self.__aula = aula

    @staticmethod
    def create(
        nome: str,
        descricao: str,
        cargaHoraria: int,
        professor: str,
        numeroVagas: int,
        cursoRelacionado: str,
        status: str,
    ):
        return Curso(
            nome,
            descricao,
            cargaHoraria,
            professor,
            numeroVagas,
            cursoRelacionado,
            status,
        )

    def toDto(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "cargaHoraria": self.cargaHoraria,
            "professor": self.professor,
            "numeroVagas": self.numeroVagas,
            "alunos": self.alunos,
            "cursoRelacionado": self.cursoRelacionado,
            "status": self.status,
            "aulas": self.aula 
        }
