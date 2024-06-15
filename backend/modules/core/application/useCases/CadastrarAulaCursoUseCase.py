from interceptors.LoggerInterceptor import LoggerInterceptor
from ...domain.repositories.CursoRepository import CursoRepositoryInteface
from ...domain.repositories.UsuarioRepository import UserRepositoryInteface
from ...domain.repositories.AulaRepository import AulaRepositoryInterface
from ...domain.Aula import Aula

class CadastarAulaCursoUseCaseRequest:
    def __init__(
        self,
        cursoId: str,
        tipoAcesso: str,
        professorId: str,
        nomeAula: str,
        descricaoAula: str,
        conteudoAula: str,
        duracaoAula: int
    ):
        self.cursoId = cursoId
        self.tipoAcesso = tipoAcesso
        self.professorId = professorId
        self.nomeAula = nomeAula
        self.descricaoAula = descricaoAula
        self.conteudoAula = conteudoAula
        self.duracaoAula = duracaoAula

    def __getitem__(self, key):
        return getattr(self, key)

@LoggerInterceptor()
class CadastarAulaCursoUseCase:
    def __init__(self, cursoRepository: CursoRepositoryInteface, usuarioRepository: UserRepositoryInteface, aulasRepository: AulaRepositoryInterface):
        self.cursoRepository = cursoRepository
        self.usuarioRepository = usuarioRepository
        self.aulasRepository = aulasRepository

    async def execute(self, request: CadastarAulaCursoUseCaseRequest) -> str:
        try:
            if request["tipoAcesso"] not in ["ADMIN", "PROFESSOR"]:
                raise ValueError("Somente administradores e professores podem cadastrar aulas em cursos")
            

            curso = self.cursoRepository.find(request["cursoId"])
            
            usuarioCadastro = self.usuarioRepository.find(request["professorId"])

            permiteCadastroAula = usuarioCadastro.validarUsuarioCriacaoCurso()
            if permiteCadastroAula == False:
                raise ValueError("O usuário não pode cadastrar cursos")
            
            aula = Aula.create(
                nome = request["nomeAula"],
                descricao = request["descricaoAula"],
                conteudo = request["conteudoAula"],
                duracao = request["duracaoAula"],
            )

            curso.cadastrarAula(aula)
            self.aulasRepository.saveList(curso.aula, curso.id)

            return curso.toDto()
        except Exception as e:
            raise e
