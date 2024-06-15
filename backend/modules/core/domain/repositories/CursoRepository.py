from ...domain.Curso import Curso
from typing import List

class CursoRepositoryInteface:
    def salvarCurso(self, curso: Curso) -> str:
        pass

    def atualizarCurso(self, curso: Curso) -> str:
        pass

    def buscarPorId(self, cursoId: str) -> Curso:
        pass

    def buscarTodos(self, pagina: int) -> List[Curso]:
        pass

    def removerPorId(self, cursoId: str) -> str:
        pass

    def buscarPorStatus(self, status: str, pagina: int) -> List[Curso]:
        pass

    def buscarNumeroDePaginas(self,) -> int:
        pass

    def inserirAlunoCurso(self, curso: Curso) -> str:
        pass

    def removerAlunoCurso(self, curso: Curso, alunoRemovido: str):
        pass
