from ...domain.Curso import Curso


class NenhumCursoCadastradoException(Exception):
    pass


class CursoMapper:
    def modelToDomain(self, cursoModel: dict):
        curso = Curso.create(
            cursoModel["cpf"],
            cursoModel["nome"],
            cursoModel["email"],
            cursoModel["senha"],
            cursoModel["dataNascimento"],
            cursoModel["ra"]
        )
        return curso