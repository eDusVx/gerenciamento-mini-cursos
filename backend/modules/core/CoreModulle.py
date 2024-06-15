from .infra.repositories.UsuarioRepository import UserRepositoryImpl
from .domain.repositories.UsuarioRepository import UserRepositoryInteface
from .infra.repositories.CursoRepository import CursoRepositoryImpl
from .infra.repositories.AulaRepository import AulaRepositoryImpl
from .domain.repositories.CursoRepository import CursoRepositoryInteface
from .domain.repositories.AulaRepository import AulaRepositoryInterface
from .application.useCases.RegistrarCursoUseCase import RegistrarCursoUsecase
from .application.useCases.RemoverUsuarioUseCase import RemoverUsuarioUsecase
from .application.useCases.AtualizarUsuarioUseCase import AtualizarUsuarioUseCase
from .application.useCases.AtualizarCursoUseCase import AtualizarCursoUseCase
from .application.useCases.RemoverCursoUseCase import RemoverCursoUsecase
from .application.queries.BuscarCursosQuery import BuscarCursosQuery
from .application.queries.BuscarUsuariosQuery import BuscarUsuariosQuery
from .application.useCases.InscreverAlunoCursoUseCase import InscreverAlunoCursoUseCase
from .infra.mappers.UsuarioMapper import UsuarioMapper
from .infra.mappers.CursoMapper import CursoMapper
from .infra.mappers.AulaMapper import AulaMapper
from .application.useCases.RemoverAlunoCursoUseCase import RemoverAlunoCursoUseCase
from .application.useCases.CadastrarAulaCursoUseCase import CadastarAulaCursoUseCase
from .application.useCases.RemoverAulaCursoUseCase import RemoverAulaCursoUseCase


class DependencyContainer:
    @staticmethod
    def provide_user_repository() -> UserRepositoryInteface:
        usuarioMapper = UsuarioMapper()
        return UserRepositoryImpl(usuarioMapper)
    
    def provide_aula_repository() -> AulaRepositoryInterface:
        return AulaRepositoryImpl()
    
    def provide_curso_repository() -> CursoRepositoryInteface:
        aulaMapper = AulaMapper()
        cursoMapper = CursoMapper(aulaMapper)
        return CursoRepositoryImpl(cursoMapper)


class UseCaseFactory:
    @staticmethod
    def createRegistrarCursoUseCase() -> RegistrarCursoUsecase:
        curso_repository = DependencyContainer.provide_curso_repository()
        return RegistrarCursoUsecase(curso_repository)

    def createAtualizarCursoUseCase() -> AtualizarCursoUseCase:
        curso_repository = DependencyContainer.provide_curso_repository()
        return AtualizarCursoUseCase(curso_repository)

    def createRemoverUsuarioUseCase() -> RemoverUsuarioUsecase:
        user_repository = DependencyContainer.provide_user_repository()
        return RemoverUsuarioUsecase(user_repository)
    
    def createAtualizarUsuarioUseCase() -> AtualizarUsuarioUseCase:
        user_repository = DependencyContainer.provide_user_repository()
        return AtualizarUsuarioUseCase(user_repository)

    def createRemoverCursoUseCase() -> RemoverCursoUsecase:
        curso_repository = DependencyContainer.provide_curso_repository()
        return RemoverCursoUsecase(curso_repository)

    def createBuscarCursosQuery() -> BuscarCursosQuery:
        curso_repository = DependencyContainer.provide_curso_repository()
        return BuscarCursosQuery(curso_repository)

    def createBuscarUsuariosQuery() -> BuscarUsuariosQuery:
        user_repository = DependencyContainer.provide_user_repository()
        return BuscarUsuariosQuery(user_repository)
    
    def createInscreverAlunoCursoUseCase() -> InscreverAlunoCursoUseCase:
        user_repository = DependencyContainer.provide_user_repository()
        curso_repository = DependencyContainer.provide_curso_repository()
        return InscreverAlunoCursoUseCase(curso_repository, user_repository)
    
    def createRemoverAlunoCursoUseCase() -> RemoverAlunoCursoUseCase:
        user_repository = DependencyContainer.provide_user_repository()
        curso_repository = DependencyContainer.provide_curso_repository()
        return RemoverAlunoCursoUseCase(curso_repository, user_repository)
    
    def createCadastrarAulaCursoUseCase() -> CadastarAulaCursoUseCase:
        user_repository = DependencyContainer.provide_user_repository()
        curso_repository = DependencyContainer.provide_curso_repository()
        aula_repository = DependencyContainer.provide_aula_repository()
        return CadastarAulaCursoUseCase(curso_repository, user_repository, aula_repository)

    def createRemoverAulaCursoUseCase() -> RemoverAulaCursoUseCase:
        user_repository = DependencyContainer.provide_user_repository()
        curso_repository = DependencyContainer.provide_curso_repository()
        aula_repository = DependencyContainer.provide_aula_repository()
        return RemoverAulaCursoUseCase(curso_repository, user_repository, aula_repository)
    

