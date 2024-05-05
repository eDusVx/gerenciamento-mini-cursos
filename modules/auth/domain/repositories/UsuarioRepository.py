from ..Usuario import Usuario
class UserRepositoryInteface:
    def buscarPorEmail(self, email: str) -> Usuario:
        pass
    def save(self,user:Usuario) -> str:
        pass

