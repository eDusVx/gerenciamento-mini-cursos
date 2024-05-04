from .infra.repositories.UsuarioRepository import UserRepositoryImpl
from .domain.repositories.UsuarioRepository import UserRepositoryInteface
from .application.useCases.RegistrarUsuarioUseCase import RegistrarUsuarioUseCase

class DependencyContainer:
    @staticmethod
    def provide_user_repository() -> UserRepositoryInteface:
        return UserRepositoryImpl()

class UseCaseFactory:
    @staticmethod
    def create_registrar_usuario_use_case() -> RegistrarUsuarioUseCase:
        user_repository = DependencyContainer.provide_user_repository()
        return RegistrarUsuarioUseCase(user_repository)