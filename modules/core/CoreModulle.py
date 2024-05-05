from .infra.repositories.UsuarioRepository import UserRepositoryImpl
from .domain.repositories.UsuarioRepository import UserRepositoryInteface
from .application.queries.BuscarCategoriaQuery import BuscarCategoriasQuery

class DependencyContainer:
    @staticmethod
    def provide_user_repository() -> UserRepositoryInteface:
        return UserRepositoryImpl()

class UseCaseFactory:
    @staticmethod
    def create_buscar_categorias_query() -> BuscarCategoriasQuery:
        user_repository = DependencyContainer.provide_user_repository()
        return BuscarCategoriasQuery(user_repository)