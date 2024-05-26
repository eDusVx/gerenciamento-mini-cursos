from interceptors.LoggerInterceptor import LoggerInterceptor
from ...domain.repositories.UsuarioRepository import UserRepositoryInteface
from ...domain.Curso import Curso, Categoria


class RegistrarCursoUseCaseRequest:
    def __init__(
        self,
        nome: str,
        descricao: str,
        cargaHoraria: str,
        professorId: str,
        numeroVagas: int,
        categoria: str,
    ):
        self.nome = nome
        self.descricao = descricao
        self.cargaHoraria = cargaHoraria
        self.professorId = professorId
        self.numeroVagas = numeroVagas
        self.categoria = categoria

    def __getitem__(self, key):
        return getattr(self, key)


@LoggerInterceptor()
class RegistrarCursoUsecase:
    def __init__(self, usuario_repository: UserRepositoryInteface):
        self.usuario_repository = usuario_repository

    async def execute(self, request: RegistrarCursoUseCaseRequest) -> str:
        try:
            professor = self.usuario_repository.find(request["professorId"])

            if professor is None:
                raise ValueError("Nenhum professor encontrado com esse id!")
            curso = Curso.create(
                nome=request["nome"],
                descricao=request["descricao"],
                cargaHoraria=request["cargaHoraria"],
                professorId=request["professorId"],
                numeroVagas=request["numeroVagas"],
                categoria=Categoria[request["categoria"]],
            )

            return curso.toDto()
        except Exception as e:
            raise e
