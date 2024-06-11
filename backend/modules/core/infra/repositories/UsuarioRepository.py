from ...domain.Usuario import Usuario
from ...domain.repositories.UsuarioRepository import UserRepositoryInteface
from dbconfig import Database
from ..mappers.UsuarioMapper import UsuarioMapper, NenhumUsuarioCadastradoException


class UserRepositoryImpl(UserRepositoryInteface):
    def __init__(self, usuario_mapper: UsuarioMapper):
        self.usuario_mapper = usuario_mapper

    def save(self, user: Usuario):
        try:
            connection = Database.obter_conexao()
            cursor = connection.cursor()
            sql = "INSERT INTO usuarios (cpf, nome, email, senha, tipoAcesso) VALUES (%s, %s, %s, %s, %s)"
            val = (user.cpf, user.nome, user.email, user.senha, user.tipoAcesso.name)
            cursor.execute(sql, val)
            connection.commit()
            cursor.close()
            return f"Usuario {user.nome} salvo com sucesso!"
        except Exception as e:
            raise Exception(f"Erro ao salvar usuário: {e}")

    def find(self, usuarioId: str):
        try:
            print(f"buscando usuario de ra = {usuarioId}")
            connection = Database.obter_conexao()
            cursor = connection.cursor(dictionary=True)
            sql = "SELECT*FROM usuarios WHERE ra = %s"
            val = (usuarioId,)
            cursor.execute(sql, val)
            result = cursor.fetchone()

            if result:
                usuario = self.usuario_mapper.modelToDomain(result)
                return usuario
            else:
                raise NenhumUsuarioCadastradoException(
                    f"Nenhum usuário cadastrado para o ra {usuarioId}"
                )
        except Exception as e:
            raise Exception(f"Erro ao buscar usuário: {e}")
    
    def remove(self, usuarioId: str):
        try:
            connection = Database.obter_conexao()
            cursor = connection.cursor()
            sql = "DELETE FROM usuarios WHERE ra = %s"
            val = (usuarioId,)
            print(sql)
            cursor.execute(sql, val)
            connection.commit()

        except Exception as e:
            raise Exception(f"Erro ao deletar usuário: {e}")
