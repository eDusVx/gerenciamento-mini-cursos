from interceptors.LoggerInterceptor import LoggerInterceptor
from ...domain.repositories.UsuarioRepository import UserRepositoryInteface
from ..services.AuthService import AuthServiceInterface


@LoggerInterceptor()
class EfetuarLoginUsuarioUsecase:
    def __init__(
        self,
        usuario_repository: UserRepositoryInteface,
        authService: AuthServiceInterface,
    ):
        self.usuario_repository = usuario_repository
        self.authService = authService

    async def execute(self, email: str, senha: str) -> str:
        try:
            usuario = self.usuario_repository.buscarPorEmail(email)
            validarSenha = usuario.validarSenha(senha)
            if validarSenha == True:
                token = self.authService.autenticar(
                    usuario.nome, usuario.email, usuario.cpf, usuario.tipoAcesso
                )
                return token
            else:
                raise Exception("Senha incorreta")
        except Exception as e:
            raise e
