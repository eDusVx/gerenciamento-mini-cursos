from ...domain.Usuario import Usuario
from typing import List

class UserRepositoryInteface:
    def buscarPorId(self, userId: str) -> Usuario:
        pass

    def removerPorId(self, userId) -> str:
        pass

    def atualizarUsuario(self, user: Usuario) -> str:
        pass

    def buscarNumeroDePaginas(self,) -> int:
        pass

    def buscarTodos(self, pagina: int) -> List[Usuario]:
        pass

    def buscarPorTipoAcesso(self, tipoAcesso: str, pagina: int) -> List[Usuario]:
        pass

    def buscarTodosPorTipo(self, tipoAcesso: str) -> List[Usuario]:
        pass
