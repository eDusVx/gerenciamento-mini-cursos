from ...domain.Curso import Curso


class CursoRepositoryInteface:
    def save(self, curso: Curso) -> str:
        pass

    def update(self, curso: Curso) -> str:
        pass

    def find(self, cursoId: str) -> Curso:
        pass

    def findAll(self, pagina: int) -> list:
        pass

    def remove(self, cursoId: str) -> str:
        pass

    def findByStatus(self, status: str, pagina: int) -> list:
        pass

    def findPagesNumber(self,) -> int:
        pass

    def inserirAlunoCurso(self, curso: Curso) -> str:
        pass

    def removerAlunoCurso(self, curso: Curso, alunoRemovido: str):
        pass
