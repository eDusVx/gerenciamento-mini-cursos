from ...domain.Usuario import Usuario
from ...domain.repositories.UsuarioRepository import UserRepositoryInteface
from dbconfig import Database

class UserRepositoryImpl(UserRepositoryInteface):
    def save(self, user: Usuario):
        try:
            connection = Database.obter_conexao()
            cursor = connection.cursor()
            sql = "INSERT INTO usuarios (cpf, nome, email, senha, tipoAcesso) VALUES (%s, %s, %s, %s, %s)"
            val = (user.cpf, user.nome, user.email, user.senha, user.tipoAcesso.name)
            cursor.execute(sql, val)
            connection.commit()
            cursor.close()
            return f'Usuario {user.nome} salvo com sucesso!'
        except Exception as e:
            raise Exception(f"Erro ao salvar usuário: {e}")
