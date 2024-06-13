from interceptors.LoggerInterceptor import LoggerInterceptor
from ...domain.repositories.CursoRepository import CursoRepositoryInteface

class BuscarCursosQueryRequest:
    def __init__(self, status: str, pagina: int):
        self.status = status
        self.pagina = pagina

    def __getitem__(self, key):
        return getattr(self, key)


@LoggerInterceptor()
class BuscarCursosQuery:
    def __init__(self, curso_repository: CursoRepositoryInteface):
        self.curso_repository = curso_repository

    async def execute(self, request: BuscarCursosQueryRequest) -> dict:
        try:
            cursos = []
            if(request["status"] == None):
                curso = self.curso_repository.findAll(request["pagina"])
                for i in curso:
                    cursos.append(i.toDto())
                return cursos
            
            curso = self.curso_repository.findByStatus(request["status"], request["pagina"])

            for i in curso:
                cursos.append(i.toDto())

            return cursos
        except Exception as e:
            raise e
