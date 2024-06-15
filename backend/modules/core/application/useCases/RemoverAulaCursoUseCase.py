from interceptors.LoggerInterceptor import LoggerInterceptor
from ...domain.repositories.CursoRepository import CursoRepositoryInteface
from ...domain.repositories.UsuarioRepository import UserRepositoryInteface
from ...domain.repositories.AulaRepository import AulaRepositoryInterface

class RemoverAulaCursoUseCaseRequest:
    def __init__(
        self,
        cursoId: str,
        tipoAcesso: str,
        professorId: str,
        aulaId: str
    ):
        self.cursoId = cursoId
        self.tipoAcesso = tipoAcesso
        self.professorId = professorId
        self.aulaId = aulaId

    def __getitem__(self, key):
        return getattr(self, key)

@LoggerInterceptor()
class RemoverAulaCursoUseCase:
    def __init__(self, cursoRepository: CursoRepositoryInteface, usuarioRepository: UserRepositoryInteface, aulasRepository: AulaRepositoryInterface):
        self.cursoRepository = cursoRepository
        self.usuarioRepository = usuarioRepository
        self.aulasRepository = aulasRepository

    async def execute(self, request: RemoverAulaCursoUseCaseRequest) -> str:
        try:
            if request["tipoAcesso"] not in ["ADMIN", "PROFESSOR"]:
                raise ValueError("Somente administradores e professores podem cadastrar aulas em cursos")
            

            curso = self.cursoRepository.buscarPorId(request["cursoId"])
            
            usuarioCadastro = self.usuarioRepository.buscarPorId(request["professorId"])
            
            permiteCadastroAula = usuarioCadastro.validarUsuarioCriacaoCurso()
            if permiteCadastroAula == False:
                raise ValueError("O usuário não pode cadastrar cursos")
            
            aulaRemovida = curso.removerAula(request["aulaId"])

            if aulaRemovida == None:
                raise ValueError("Erro ao remover aula")
            
            self.aulasRepository.removerAula(str(curso.id), aulaRemovida)

            return curso.toDto()
        except Exception as e:
            raise e
