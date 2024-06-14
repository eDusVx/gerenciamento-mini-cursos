from ...domain.Usuario import Usuario


class UserRepositoryInteface:
    def find(self, userId: str) -> Usuario:
        pass

    def remove(self, userId) -> str:
        pass

    def update(self, user: Usuario) -> str:
        pass

    def findPagesNumber(self,) -> int:
        pass

    def findAll(self, pagina: int) -> list:
        pass

    def findByTipoAcesso(self, tipoAcesso: str, pagina: int) -> list:
        pass
