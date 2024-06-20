from interceptors.LoggerInterceptor import LoggerInterceptor
from ...domain.repositories.UsuarioRepository import UserRepositoryInteface
from ..services.AuthService import AuthServiceInterface


class EfetuarLoginUsuarioUseCaseRequest:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def __getitem__(self, key):
        return getattr(self, key)

@LoggerInterceptor()
class EfetuarLoginUsuarioUsecase:
    def __init__(
        self,
        usuario_repository: UserRepositoryInteface,
        authService: AuthServiceInterface,
    ):
        self.usuario_repository = usuario_repository
        self.authService = authService

    async def execute(self, request: EfetuarLoginUsuarioUseCaseRequest) -> str:
        try:
            usuario = self.usuario_repository.buscarPorEmail(request["email"])
            validarSenha = usuario.validarSenha(request["senha"])
            if validarSenha == True:
                token = self.authService.autenticar(
                    usuario.nome, usuario.email, usuario.cpf, usuario.tipoAcesso
                )
                return token
            else:
                raise Exception("Usuário ou senha inválidos")
        except Exception as e:
            raise e
