from interceptors.LoggerInterceptor import LoggerInterceptor
from ...domain.repositories.CursoRepository import CursoRepositoryInteface
from ...domain.repositories.UsuarioRepository import UserRepositoryInteface
from ...domain.Curso import Curso

class InscreverAlunoCursoUseCaseRequest:
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
class InscreverAlunoCursoUseCase:
    def __init__(self, cursoRepository: CursoRepositoryInteface, usuarioRepository: UserRepositoryInteface):
        self.cursoRepository = cursoRepository
        self.usuarioRepository = usuarioRepository

    async def execute(self, request: InscreverAlunoCursoUseCaseRequest) -> str:
        try:
            if request["tipoAcesso"] not in ["ADMIN", "PROFESSOR"]:
                raise ValueError("Somente administradores e professores podem inscrever alunos em cursos")
            curso = self.cursoRepository.find(request["cursoId"])
            aluno = self.usuarioRepository.find(request["ra"])

            curso.inscreverAluno(aluno)
            
            self.cursoRepository.inserirAlunoCurso(curso)

            return curso.toDto()
        except Exception as e:
            raise e
