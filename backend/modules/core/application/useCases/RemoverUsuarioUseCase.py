from interceptors.LoggerInterceptor import LoggerInterceptor
from ...domain.repositories.UsuarioRepository import UserRepositoryInteface

class RemoverUsuarioUseCaseRequest:
    def __init__(
        self,
        ra: str,
        tipoAcesso: str,
    ):
        self.ra = ra
        self.tipoAcesso = tipoAcesso

    def __getitem__(self, key):
        return getattr(self, key)

@LoggerInterceptor()
class RemoverUsuarioUsecase:
    def __init__(self, usuario_repository: UserRepositoryInteface):
        self.usuario_repository = usuario_repository

    async def execute(self, request: RemoverUsuarioUseCaseRequest) -> str:
        try:
            if request["tipoAcesso"] != "ADMIN":
                raise ValueError("Somente administradores podem remover usuários")
           
            usuario = self.usuario_repository.find(request["ra"])
        # TODO terminar remoção de usuários
            return f"Usuário ra : {request["ra"]} removido com sucesso!"
        except Exception as e:
            raise e
