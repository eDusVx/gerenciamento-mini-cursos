from ...domain.Usuario import Usuario, TipoAcesso

class NenhumUsuarioCadastradoException(Exception):
    pass

class UsuarioMapper():
    def modelToDomain(self, usuarioModel: dict):
        usuario = Usuario.create(usuarioModel['cpf'], usuarioModel['nome'], usuarioModel['email'], usuarioModel['senha'], TipoAcesso[usuarioModel['tipoAcesso']])
        return usuario
