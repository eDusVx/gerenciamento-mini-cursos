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
            buscarNumeroPaginas = self.curso_repository.buscarNumeroDePaginas(request["status"] if request["status"] else None)
            if(request["status"] == None):
                curso = self.curso_repository.buscarTodos(request["pagina"])
                for i in curso:
                    cursos.append(i.toDto())
                return {"cursos": cursos, "numeroPaginas": buscarNumeroPaginas}
            
            curso = self.curso_repository.buscarPorStatus(request["status"], request["pagina"])

            for i in curso:
                cursos.append(i.toDto())

            return {"cursos": cursos, "numeroPaginas": buscarNumeroPaginas}
        except Exception as e:
            raise e
