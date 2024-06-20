import hashlib
from enum import Enum
from datetime import date, datetime
from typing import Optional

class TipoAcesso(Enum):
    ADMIN = "ADMIN"
    ALUNO = "ALUNO"
    PROFESSOR = "PROFESSOR"


class Sexo(Enum):
    M = "MASCULINO"
    F = "FEMININO"


class Usuario:
    def __init__(
        self, cpf: str, nome: str, email: str, senha: str, tipoAcesso: TipoAcesso, dataNascimento: date, sexo: Sexo, ra: str, dataInclusao: Optional[datetime] = None,
    ):
        self.__cpf = cpf
        self.nome = nome
        self.email = email
        self.__senha = senha if len(senha) == 64 else self.__criptografar_senha(senha)
        self.tipoAcesso = tipoAcesso
        self.sexo = sexo
        self.dataNascimento = dataNascimento
        self.ra = ra
        self.dataInclusao = dataInclusao

    @property
    def cpf(self):
        return self.__cpf

    @property
    def dataInclusao(self):
        return self.__dataInclusao

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
    
    @property
    def sexo(self):
        return self.__sexo
    
    @property
    def dataNascimento(self):
        return self.__dataNascimento
    
    @property
    def ra(self):
        return self.__ra

    @dataInclusao.setter
    def dataInclusao(self, dataInclusao: Optional[datetime]):
        if dataInclusao is None:
            self.__dataInclusao = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        else:
            self.__dataInclusao = dataInclusao

    @nome.setter
    def nome(self, nome: str):
        if not nome:
            raise ValueError("Nome não informado!")
        if not isinstance(nome, str):
            raise ValueError("Nome deve ser uma string!")
        self.__nome = nome

    @email.setter
    def email(self, email: str):
        if not email:
            raise ValueError("Email não informado!")
        if not isinstance(email, str):
            raise ValueError("Email deve ser uma string!")
        if "@" not in email or "." not in email:
            raise ValueError("Email inválido!")
        self.__email = email

    @senha.setter
    def senha(self, senha: str):
        if not senha:
            raise ValueError("Senha não informada!")
        if len(senha) < 6:
            raise ValueError("Senha deve ter pelo menos 6 caracteres!")
        self.__senha = senha

    @tipoAcesso.setter
    def tipoAcesso(self, tipoAcesso: TipoAcesso):
        if not tipoAcesso:
            raise ValueError("Tipoacesso não informado!")
        if not isinstance(tipoAcesso, TipoAcesso):
            raise ValueError("Tipo de acesso inválido!")
        self.__tipoAcesso = tipoAcesso
    
    @sexo.setter
    def sexo(self, sexo: Sexo):
        if not sexo:
            raise ValueError("Sexo não informado!")
        if not isinstance(sexo, Sexo):
            raise ValueError("Sexo inválido!")
        self.__sexo = sexo

    @dataNascimento.setter
    def dataNascimento(self, dataNascimento: datetime):
        if not dataNascimento:
            raise ValueError("Data de nascimento não informada!")
        if not isinstance(dataNascimento, date):
            raise ValueError("Data de nascimento inválida!")
        self.__dataNascimento = dataNascimento
    
    @cpf.setter
    def cpf(self, cpf: str):
        if not cpf:
            raise ValueError("CPF não informado!")
        if not isinstance(cpf, str) or not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("CPF inválido!")
        
        self.__cpf = cpf
    
    @ra.setter
    def ra(self, ra: str):
        if not ra:
            raise ValueError("RA não informado!")
        
        self.__ra = ra

    def __criptografar_senha(self, senha: str) -> str:
        return hashlib.sha256(senha.encode()).hexdigest()

    @staticmethod
    def create(cpf: str, nome: str, email: str, senha: str, tipoAcesso: TipoAcesso, dataNascimento: date, sexo: Sexo, ra: str):
        return Usuario(cpf, nome, email, senha, tipoAcesso, dataNascimento, sexo, ra)

    def validarSenha(self, senha: str) -> bool:
        if self.senha == hashlib.sha256(senha.encode()).hexdigest():
            return True
        else:
            return False
