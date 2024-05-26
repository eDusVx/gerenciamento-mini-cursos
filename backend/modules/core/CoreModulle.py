from .infra.repositories.UsuarioRepository import UserRepositoryImpl
from .domain.repositories.UsuarioRepository import UserRepositoryInteface
from .application.useCases.RegistrarCursoUseCase import RegistrarCursoUsecase
from .infra.mappers.UsuarioMapper import UsuarioMapper


class DependencyContainer:
    @staticmethod
    def provide_user_repository() -> UserRepositoryInteface:
        usuarioMapper = UsuarioMapper()
        return UserRepositoryImpl(usuarioMapper)


class UseCaseFactory:
    @staticmethod
    def createRegistrarCursoUseCase() -> RegistrarCursoUsecase:
        user_repository = DependencyContainer.provide_user_repository()
        return RegistrarCursoUsecase(user_repository)
