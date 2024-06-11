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

    def update(self, usuario: Usuario):
        try:
            connection = Database.obter_conexao()
            cursor = connection.cursor()

            fields_to_update = []
            values = []

            if usuario.cpf:
                fields_to_update.append("cpf = %s")
                values.append(usuario.cpf)
            if usuario.nome:
                fields_to_update.append("nome = %s")
                values.append(usuario.nome)
            if usuario.email:
                fields_to_update.append("email = %s")
                values.append(usuario.email)
            if usuario.senha:
                fields_to_update.append("senha = %s")
                values.append(usuario.senha)
            if usuario.dataNascimento:
                fields_to_update.append("dataNascimento = %s")
                values.append(usuario.dataNascimento)
            if usuario.sexo:
                fields_to_update.append("sexo = %s")
                values.append(usuario.sexo._name_)

            if not fields_to_update:
                raise ValueError("Nenhum campo para atualizar foi fornecido")

            values.append(usuario.ra)
            sql = f"UPDATE usuarios SET {', '.join(fields_to_update)} WHERE ra = %s"
            cursor.execute(sql, values)
            connection.commit()
        except Exception as e:
            raise Exception(f"Erro ao atualizar usuário: {e}")