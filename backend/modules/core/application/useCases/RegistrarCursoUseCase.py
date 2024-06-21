from interceptors.LoggerInterceptor import LoggerInterceptor
from ...domain.repositories.CursoRepository import CursoRepositoryInteface
from ...domain.Curso import Curso

class RegistrarCursoUseCaseRequest:
    def __init__(
        self,
        nome: str,
        descricao: str,
        cargaHoraria: str,
        professor: str,
        numeroVagas: int,
        cursoRelacionado: str,
        status: str
    ):
        self.nome = nome
        self.descricao = descricao
        self.cargaHoraria = cargaHoraria
        self.professor = professor
        self.numeroVagas = numeroVagas
        self.cursoRelacionado = cursoRelacionado
        self.status = status

    def __getitem__(self, key):
        return getattr(self, key)

@LoggerInterceptor()
class RegistrarCursoUsecase:
    def __init__(self, cursoRepository: CursoRepositoryInteface):
        self.cursoRepository = cursoRepository

    async def execute(self, request: RegistrarCursoUseCaseRequest) -> str:
        try:

            buscarCurso = self.cursoRepository.buscarPorNome(request["nome"])
            if buscarCurso == True:
                raise ValueError(f"Já existe um curso com o nome {request['nome']}!")
            
            curso = Curso.create(
                nome=request["nome"],
                descricao=request["descricao"],
                cargaHoraria=int(request["cargaHoraria"]),
                professor=request["professor"],
                numeroVagas=request["numeroVagas"],
                cursoRelacionado=request["cursoRelacionado"],
                status=request["status"]
            )

            self.cursoRepository.salvarCurso(curso)

            return curso.toDto()
        except Exception as e:
            raise e
