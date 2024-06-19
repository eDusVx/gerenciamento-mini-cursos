from services.base_service import BaseService

class CourseService(BaseService):
    def registrar_curso(self, course_data):
        return self.post("registrar-curso", json=course_data)

    def remover_curso(self, course_id):
        data = {"id": course_id}
        return self.delete("remover-curso", json=data)

    def remover_aluno_curso(self, ra, curso_id):
        data = {
            "ra": ra,
            "cursoId": curso_id
        }
        return self.delete("remover-aluno-curso", json=data)

    def remover_aula_curso(self, curso_id, professor_id, aula_id):
        data = {
            "cursoId": curso_id,
            "professorId": professor_id,
            "aulaId": aula_id
        }
        return self.delete("remover-aula-curso", json=data)

    def cadastrar_aula_curso(self, aula_data):
        return self.post("cadastrar-aula-curso", json=aula_data)

    def atualizar_usuario(self, user_data):
        return self.put("atualizar-usuario", json=user_data)

    def atualizar_curso(self, course_data):
        return self.put("atualizar-curso", json=course_data)

    def buscar_cursos(self, pagina):
        params = {"pagina": pagina}
        return self.get("buscar-cursos", params=params)

    def inscrever_aluno_curso(self, ra, curso_id):
        data = {
            "ra": ra,
            "cursoId": curso_id
        }
        return self.post("inscrever-aluno-curso", json=data)
