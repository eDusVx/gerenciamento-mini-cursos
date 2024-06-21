from .infra.repositories.UsuarioRepository import UserRepositoryImpl
from .domain.repositories.UsuarioRepository import UserRepositoryInteface
from .application.useCases.EfetuarLoginUsuarioUseCase import EfetuarLoginUsuarioUsecase
from .infra.mappers.UsuarioMapper import UsuarioMapper
from .domain.services.AuthService import AuthService
from .application.services.AuthService import AuthServiceInterface
from .application.useCases.RegistrarUsuarioUseCase import RegistrarUsuarioUseCase
from .application.useCases.RecuperarSeanhaUseCase import RecuperarSenhaUseCase


class DependencyContainer:
    @staticmethod
    def provide_user_repository() -> UserRepositoryInteface:
        usuarioMapper = UsuarioMapper()
        return UserRepositoryImpl(usuarioMapper)

    def provide_auth_service() -> AuthServiceInterface:
        return AuthService()


class UseCaseFactory:
    @staticmethod
    def create_efetuar_login_usuario_use_case() -> EfetuarLoginUsuarioUsecase:
        user_repository = DependencyContainer.provide_user_repository()
        authService = DependencyContainer.provide_auth_service()
        return EfetuarLoginUsuarioUsecase(user_repository, authService)

    def create_registrar_usuario_use_case() -> RegistrarUsuarioUseCase:
        user_repository = DependencyContainer.provide_user_repository()
        return RegistrarUsuarioUseCase(user_repository)

    def create_recuperar_senha_use_case() -> RecuperarSenhaUseCase:
        user_repository = DependencyContainer.provide_user_repository()
        return RecuperarSenhaUseCase(user_repository)
