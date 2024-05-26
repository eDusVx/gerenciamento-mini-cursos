from ...domain.Usuario import Usuario, TipoAcesso, Sexo


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
            usuarioModel["ra"]
        )
        return usuario
