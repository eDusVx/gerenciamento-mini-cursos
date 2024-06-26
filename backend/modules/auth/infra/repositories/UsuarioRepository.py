from ...domain.repositories.UsuarioRepository import UserRepositoryInteface
from ..mappers.UsuarioMapper import UsuarioMapper
from dbconfig import Database
from ...domain import Usuario
from datetime import datetime


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

    def salvar(self, user: Usuario):
        try:
            connection = Database.obter_conexao()
            cursor = connection.cursor()
            sql = "INSERT INTO usuarios (cpf, nome, email, senha, tipoAcesso, dataNascimento, sexo, ra, data_inclusao, data_modificacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (user.cpf, user.nome, user.email, user.senha, user.tipoAcesso.name, user.dataNascimento, user.sexo.name, user.ra, user.dataInclusao, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
            cursor.execute(sql, val)
            connection.commit()
            cursor.close()
            return f"Usuario {user.nome} salvo com sucesso!"
        except Exception as e:
            raise Exception(f"Erro ao salvar usuário: {e}")
        
    def salvarNovaSenha(self, user: Usuario):
        try:
            connection = Database.obter_conexao()
            cursor = connection.cursor()
            sql = "UPDATE usuarios SET senha = %s, data_modificacao = %s WHERE email = %s"
            val = (user.senha, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), user.email)
            cursor.execute(sql, val)
            connection.commit()
            cursor.close()
            return "Senha alterada com sucesso!"
        except Exception as e:
            raise Exception(f"Erro ao salvar nova senha: {e}")
