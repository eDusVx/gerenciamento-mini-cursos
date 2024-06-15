from interceptors.LoggerInterceptor import LoggerInterceptor
from ...domain.repositories.CursoRepository import CursoRepositoryInteface
from ...domain.repositories.UsuarioRepository import UserRepositoryInteface

class RemoverAlunoCursoUseCaseRequest:
    def __init__(
        self,
        ra: str,
        cursoId: str,
        tipoAcesso: str
    ):
        self.ra = ra
        self.cursoId = cursoId
        self.tipoAcesso = tipoAcesso

    def __getitem__(self, key):
        return getattr(self, key)

@LoggerInterceptor()
class RemoverAlunoCursoUseCase:
    def __init__(self, cursoRepository: CursoRepositoryInteface, usuarioRepository: UserRepositoryInteface):
        self.cursoRepository = cursoRepository
        self.usuarioRepository = usuarioRepository

    async def execute(self, request: RemoverAlunoCursoUseCaseRequest) -> str:
        try:
            if request["tipoAcesso"] not in ["ADMIN", "PROFESSOR"]:
                raise ValueError("Somente administradores e professores podem remover alunos em cursos")
            
            curso = self.cursoRepository.buscarPorId(request["cursoId"])
            aluno = self.usuarioRepository.buscarPorId(request["ra"])

            alunoRemovido = curso.removerAluno(aluno)
            
            self.cursoRepository.removerAlunoCurso(curso, alunoRemovido)

            return curso.toDto()
        except Exception as e:
            raise e
