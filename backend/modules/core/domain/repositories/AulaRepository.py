from ...domain.Aula import Aula
from typing import List


class AulaRepositoryInterface:
    def saveList(self, aula: List[Aula], cursoId: str) -> str:
        pass

