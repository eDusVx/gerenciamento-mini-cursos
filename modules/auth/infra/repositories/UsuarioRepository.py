from ...domain.repositories.UsuarioRepository import UserRepositoryInteface
from ..mappers.UsuarioMapper import UsuarioMapper
from dbconfig import Database

class NenhumUsuarioCadastradoException(Exception):
    pass

class UserRepositoryImpl(UserRepositoryInteface):
    def __init__(self, usuario_mapper: UsuarioMapper):
        self.usuario_mapper = usuario_mapper

    def buscarPorEmail(self, email: str):
        try:
            connection = Database.obter_conexao()
            cursor = connection.cursor(dictionary=True)
            sql = "SELECT * FROM teste_ddd.usuarios WHERE email = %s"
            val = (email,)
            cursor.execute(sql, val)
            result = cursor.fetchone() 

            if result:
                usuario = self.usuario_mapper.modelToDomain(result)
                return usuario
            else:
                raise NenhumUsuarioCadastradoException(f"Nenhum usuário cadastrado para o email {email}") 
        except NenhumUsuarioCadastradoException as e:
            raise e
        except Exception as e:
            raise Exception("Erro ao buscar usuário.")
