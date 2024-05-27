from .infra.repositories.UsuarioRepository import UserRepositoryImpl
from .domain.repositories.UsuarioRepository import UserRepositoryInteface
from .infra.repositories.CursoRepository import CursoRepositoryImpl
from .domain.repositories.CursoRepository import CursoRepositoryInteface
from .application.useCases.RegistrarCursoUseCase import RegistrarCursoUsecase
from .infra.mappers.UsuarioMapper import UsuarioMapper
from .infra.mappers.CursoMapper import CursoMapper


class DependencyContainer:
    @staticmethod
    def provide_user_repository() -> UserRepositoryInteface:
        usuarioMapper = UsuarioMapper()
        return UserRepositoryImpl(usuarioMapper)
    
    def provide_curso_repository() -> CursoRepositoryInteface:
        cursoMapper = CursoMapper()
        return CursoRepositoryImpl(cursoMapper)


class UseCaseFactory:
    @staticmethod
    def createRegistrarCursoUseCase() -> RegistrarCursoUsecase:
        curso_repository = DependencyContainer.provide_curso_repository()
        return RegistrarCursoUsecase(curso_repository)
