from ...domain.repositories.UsuarioRepository import UserRepositoryInteface
from ..mappers.UsuarioMapper import UsuarioMapper
from dbconfig import Database
from ...domain import Usuario


class NenhumUsuarioCadastradoException(Exception):
    pass


class UserRepositoryImpl(UserRepositoryInteface):
    def __init__(self, usuario_mapper: UsuarioMapper):
        self.usuario_mapper = usuario_mapper

    def buscarPorEmail(self, email: str):
        try:
            connection = Database.obter_conexao()
            cursor = connection.cursor(dictionary=True)
            sql = "SELECT * FROM usuarios WHERE email = %s"
            val = (email,)
            cursor.execute(sql, val)
            result = cursor.fetchone()

            if result:
                usuario = self.usuario_mapper.modelToDomain(result)
                return usuario
            else:
                raise NenhumUsuarioCadastradoException(
                    f"Nenhum usuário cadastrado para o email {email}"
                )
        except NenhumUsuarioCadastradoException as e:
            raise e
        except Exception as e:
            raise Exception("Erro ao buscar usuário.")

    def save(self, user: Usuario):
        try:
            connection = Database.obter_conexao()
            cursor = connection.cursor()
            sql = "INSERT INTO usuarios (cpf, nome, email, senha, tipoAcesso, dataNascimento, sexo, ra) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (user.cpf, user.nome, user.email, user.senha, user.tipoAcesso.name, user.dataNascimento, user.sexo.name, user.ra)
            cursor.execute(sql, val)
            connection.commit()
            cursor.close()
            return f"Usuario {user.nome} salvo com sucesso!"
        except Exception as e:
            raise Exception(f"Erro ao salvar usuário: {e}")
