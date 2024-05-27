from ...domain.Curso import Curso


class CursoRepositoryInteface:
    def save(self, curso: Curso) -> str:
        pass
