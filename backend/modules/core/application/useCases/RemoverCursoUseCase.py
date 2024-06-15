from interceptors.LoggerInterceptor import LoggerInterceptor
from ...domain.repositories.CursoRepository import CursoRepositoryInteface

class RemoverCursoUseCaseRequest:
    def __init__(
        self,
        id: str,
        tipoAcesso: str,
    ):
        self.id = id
        self.tipoAcesso = tipoAcesso

    def __getitem__(self, key):
        return getattr(self, key)

@LoggerInterceptor()
class RemoverCursoUsecase:
    def __init__(self, curso_repository: CursoRepositoryInteface):
        self.curso_repository = curso_repository

    async def execute(self, request: RemoverCursoUseCaseRequest) -> str:
        try:
            if request["tipoAcesso"] != "ADMIN":
                raise ValueError("Somente administradores podem remover cursos")
           
            self.curso_repository.removerPorId(request["id"])

            return f"Curso : {request["id"]} removido com sucesso!"
        except Exception as e:
            raise e
