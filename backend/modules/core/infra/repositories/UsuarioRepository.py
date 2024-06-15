from ...domain.Usuario import Usuario
from ...domain.repositories.UsuarioRepository import UserRepositoryInteface
from dbconfig import Database
from ..mappers.UsuarioMapper import UsuarioMapper, NenhumUsuarioCadastradoException
import os
import math
from datetime import datetime

class UserRepositoryImpl(UserRepositoryInteface):
    def __init__(self, usuario_mapper: UsuarioMapper):
        self.usuario_mapper = usuario_mapper

    def buscarPorId(self, usuarioId: str):
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
    
    def removerPorId(self, usuarioId: str):
        try:
            connection = Database.obter_conexao()
            cursor = connection.cursor()
            sql = "DELETE FROM usuarios WHERE ra = %s"
            val = (usuarioId,)
            cursor.execute(sql, val)
            connection.commit()

        except Exception as e:
            raise Exception(f"Erro ao deletar usuário: {e}")

    def atualizarUsuario(self, usuario: Usuario):
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
            
            fields_to_update.append("data_modificacao = %s")
            values.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))

            if not fields_to_update:
                raise ValueError("Nenhum campo para atualizar foi fornecido")

            values.append(usuario.ra)
            sql = f"UPDATE usuarios SET {', '.join(fields_to_update)} WHERE ra = %s"
            cursor.execute(sql, values)
            connection.commit()
        except Exception as e:
            raise Exception(f"Erro ao atualizar usuário: {e}")
    
    def buscarNumeroDePaginas(self, tipoAcesso: str):
        try:
            val = None
            connection = Database.obter_conexao()
            cursor = connection.cursor()
            tamanho_pagina = int(os.getenv("TAMANHO_PAGINA"))

            if tamanho_pagina <= 0:
                raise ValueError("TAMANHO_PAGINA must be a positive integer")

            sql = "SELECT count(*) FROM usuarios"
            if tipoAcesso is not None:
                sql = sql + " WHERE tipoAcesso = %s"
                val = (tipoAcesso,)
            cursor.execute(sql, val)
            result = cursor.fetchone()

            if result is None or len(result) == 0:
                raise ValueError("Failed to fetch count from the database")

            paginas = math.ceil(result[0] / tamanho_pagina)
            return paginas
        except Exception as e:
            raise Exception(f"Erro ao buscar número de páginas: {e}")
    

    def buscarTodos(self, pagina: int):
        try:
            tamanho_pagina = int(os.getenv("TAMANHO_PAGINA"))
            usuarios = []
            connection = Database.obter_conexao()
            cursor = connection.cursor(dictionary=True)
            offset = (pagina - 1) * tamanho_pagina
            sql = "SELECT * FROM usuarios order by data_inclusao ASC LIMIT %s OFFSET %s"
            cursor.execute(sql, (tamanho_pagina, offset))
            result = cursor.fetchall()
            if len(result) == 0:
                raise ValueError("Nenhum Usuario cadastrado")
            
            for row in result:
                usuario = self.usuario_mapper.modelToDomain(row)
                usuarios.append(usuario)
            return usuarios
        except Exception as e:
            raise Exception(f"Erro ao buscar usuarios: {e}")

    
    def buscarPorTipoAcesso(self, tipoAcesso: str, pagina: int):
        try:
            tamanho_pagina = int(os.getenv("TAMANHO_PAGINA"))
            usuarios = []
            connection = Database.obter_conexao()
            cursor = connection.cursor(dictionary=True)
            offset = (pagina - 1) * tamanho_pagina
            sql = "SELECT * FROM usuarios WHERE tipoAcesso = %s order by data_inclusao ASC LIMIT %s OFFSET %s"
            cursor.execute(sql, (tipoAcesso, tamanho_pagina, offset))
            result = cursor.fetchall()
            if len(result) == 0:
                raise ValueError("Nenhum Curso cadastrado")
            for row in result:
                usuario = self.usuario_mapper.modelToDomain(row)
                usuarios.append(usuario)
            return usuarios
        except Exception as e:
            raise Exception(f"Erro ao buscar usuarios: {e}")