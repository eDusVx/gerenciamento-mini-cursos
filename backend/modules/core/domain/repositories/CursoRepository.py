from ...domain.Curso import Curso


class CursoRepositoryInteface:
    def save(self, curso: Curso) -> str:
        pass

    def update(self, curso: Curso) -> str:
        pass

    def find(self, cursoId: str) -> Curso:
        pass
