from interceptors.LoggerInterceptor import LoggerInterceptor
from ...domain.repositories.UsuarioRepository import UserRepositoryInteface
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
    def __init__(self, usuario_repository: UserRepositoryInteface):
        self.usuario_repository = usuario_repository

    async def execute(self, request: RegistrarCursoUseCaseRequest) -> str:
        try:
            professor = self.usuario_repository.find(request["professor"])

            if professor is None:
                raise ValueError("Nenhum professor encontrado com esse id!")
            curso = Curso.create(
                nome=request["nome"],
                descricao=request["descricao"],
                cargaHoraria=int(request["cargaHoraria"]),
                professor=request["professor"],
                numeroVagas=request["numeroVagas"],
                cursoRelacionado=request["cursoRelacionado"],
                status=request["status"]
            )
            # TODO SALVAR CURSO NA BASE
            return curso.toDto()
        except Exception as e:
            raise e
