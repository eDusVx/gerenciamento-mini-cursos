from interceptors.LoggerInterceptor import LoggerInterceptor
from ...domain.Usuario import Usuario, TipoAcesso, Sexo
from ...domain.repositories.UsuarioRepository import UserRepositoryInteface
from datetime import datetime


class RegistrarUsuarioUseCaseRequest:
    def __init__(self, nome, email, senha, cpf, tipoAcesso, dataNascimento, sexo, ra):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.tipoAcesso = tipoAcesso
        self.dataNascimento = dataNascimento
        self.sexo = sexo
        self.ra = ra

    def __getitem__(self, key):
        return getattr(self, key)


@LoggerInterceptor()
class RegistrarUsuarioUseCase:
    def __init__(self, usuario_repository: UserRepositoryInteface):
        self.usuario_repository = usuario_repository

    async def execute(self, request: RegistrarUsuarioUseCaseRequest):
        try:
            if not request["cpf"]:
                raise ValueError("CPF não informado!")

            usuario = Usuario.create(
                nome=request["nome"],
                email=request["email"],
                senha=request["senha"],
                cpf=request["cpf"],
                tipoAcesso=TipoAcesso[request["tipoAcesso"]],
                dataNascimento=datetime.strptime(request["dataNascimento"], "%d-%m-%Y").date(),
                sexo=Sexo[request["sexo"]],
                ra=request["ra"]
            )

            print("SALVANDO USUARIO")
            self.usuario_repository.save(usuario)

            return f"Usuário {request['nome']} com RA {request['ra']} registrado com sucesso!"
        except Exception as e:
            raise e
