from ...domain.Usuario import Usuario


class UserRepositoryInteface:
    def save(self, user: Usuario) -> str:
        pass

    def find(self, userId: str) -> Usuario:
        pass
