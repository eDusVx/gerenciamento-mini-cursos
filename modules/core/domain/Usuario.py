import hashlib
from enum import Enum


class TipoAcesso(Enum):
    ADMIN = "ADMIN"
    ALUNO = "ALUNO"
    PROFESSOR = "PROFESSOR"


class Usuario:
    def __init__(
        self, cpf: str, nome: str, email: str, senha: str, tipoAcesso: TipoAcesso
    ):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipoAcesso = tipoAcesso

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha

    @property
    def tipoAcesso(self):
        return self.__tipoAcesso

    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError("Nome não informado!")
        if not isinstance(nome, str):
            raise ValueError("Nome deve ser uma string!")
        self.__nome = nome

    @email.setter
    def email(self, email):
        if not email:
            raise ValueError("Email não informado!")
        if not isinstance(email, str) or "@" not in email or "." not in email:
            raise ValueError("Email inválido!")
        self.__email = email

    @senha.setter
    def senha(self, senha):
        if not senha:
            raise ValueError("Senha não informada!")
        if len(senha) < 6:
            raise ValueError("Senha deve ter pelo menos 6 caracteres!")
        self.__senha = senha

    @tipoAcesso.setter
    def tipoAcesso(self, tipoAcesso):
        if not tipoAcesso:
            raise ValueError("Tipoacesso não informado!")
        if not isinstance(tipoAcesso, TipoAcesso):
            raise ValueError("Tipo de acesso inválido!")
        self.__tipoAcesso = tipoAcesso

    @cpf.setter
    def cpf(self, cpf):
        if not cpf:
            raise ValueError("Cpf não informado!")
        if not isinstance(cpf, str) or not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("CPF inválido!")
        self.__cpf = cpf

    @staticmethod
    def create(cpf: str, nome: str, email: str, senha: str, tipoAcesso: TipoAcesso):
        return Usuario(cpf, nome, email, senha, tipoAcesso)
