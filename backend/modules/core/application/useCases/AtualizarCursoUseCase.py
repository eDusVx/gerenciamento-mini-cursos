from interceptors.LoggerInterceptor import LoggerInterceptor
from ...domain.repositories.CursoRepository import CursoRepositoryInteface

class AtualizarCursoUseCaseRequest:
    def __init__(self, tipoAcesso: str, id: str, nome: str, descricao: str, cargaHoraria: int, professor: str, numeroVagas: int, cursoRelacionado: str, status: str):
        self.tipoAcesso = tipoAcesso
        self.id = id
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
class AtualizarCursoUseCase:
    def __init__(self, curso_repository: CursoRepositoryInteface):
        self.curso_repository = curso_repository

    async def execute(self, request: AtualizarCursoUseCaseRequest) -> str:
        try:
            if request["tipoAcesso"] not in ["ADMIN", "PROFESSOR"]:
                raise ValueError("Somente administradores e professores podem atualizar cursos")
            
            curso = self.curso_repository.find(request["id"])
            if curso is None:
                raise ValueError("Curso não encontrado")

            curso.atualizar_curso(
                nome=request["nome"],
                descricao=request["descricao"],
                cargaHoraria=request["cargaHoraria"],
                professor=request["professor"],
                numeroVagas=request["numeroVagas"],
                cursoRelacionado=request["cursoRelacionado"],
                status=request["status"]
            )

            self.curso_repository.update(curso)

            return f"Curso: {request['nome']} atualizado com sucesso!"
        except Exception as e:
            raise e
