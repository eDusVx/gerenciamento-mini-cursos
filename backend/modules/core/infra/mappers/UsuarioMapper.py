from ...domain.Usuario import Usuario, TipoAcesso, Sexo
from datetime import datetime


class NenhumUsuarioCadastradoException(Exception):
    pass


class UsuarioMapper:
    def modelToDomain(self, usuarioModel: dict):
        usuario = Usuario.create(
            usuarioModel["cpf"],
            usuarioModel["nome"],
            usuarioModel["email"],
            usuarioModel["senha"],
            TipoAcesso[usuarioModel["tipoAcesso"]],
            usuarioModel["dataNascimento"],
            Sexo[usuarioModel["sexo"]],
            usuarioModel["ra"],
            dataInclusao=datetime.strptime(str(usuarioModel["data_inclusao"]), '%Y-%m-%d %H:%M:%S.%f')
        )
        return usuario