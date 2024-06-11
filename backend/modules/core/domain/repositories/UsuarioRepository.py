from ...domain.Usuario import Usuario


class UserRepositoryInteface:
    def save(self, user: Usuario) -> str:
        pass

    def find(self, userId: str) -> Usuario:
        pass

    def remove(self, userId) -> str:
        pass

    def update(self, user: Usuario) -> str:
        pass
