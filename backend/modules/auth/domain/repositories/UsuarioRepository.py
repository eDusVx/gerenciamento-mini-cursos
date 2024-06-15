from ..Usuario import Usuario


class UserRepositoryInteface:
    def buscarPorEmail(self, email: str) -> Usuario:
        pass

    def salvar(self, user: Usuario) -> str:
        pass
