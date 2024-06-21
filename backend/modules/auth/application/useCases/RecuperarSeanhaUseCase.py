from interceptors.LoggerInterceptor import LoggerInterceptor
from ...domain.Usuario import Usuario, TipoAcesso, Sexo
from ...domain.repositories.UsuarioRepository import UserRepositoryInteface
from datetime import datetime


class RecuperarSenhaUseCaseRequest:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def __getitem__(self, key):
        return getattr(self, key)


@LoggerInterceptor()
class RecuperarSenhaUseCase:
    def __init__(self, usuario_repository: UserRepositoryInteface):
        self.usuario_repository = usuario_repository

    async def execute(self, request: RecuperarSenhaUseCaseRequest):
        try:
            usuario = self.usuario_repository.buscarPorEmail(request["email"])

            usuario.alterarSenha(request["senha"])

            self.usuario_repository.salvarNovaSenha(usuario)

            return f"Senha alterada com sucesso!"
        except Exception as e:
            raise e
