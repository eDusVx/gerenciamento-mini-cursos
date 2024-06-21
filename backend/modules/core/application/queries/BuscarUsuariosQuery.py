from interceptors.LoggerInterceptor import LoggerInterceptor
from ...domain.repositories.UsuarioRepository import UserRepositoryInteface

class BuscarUsuariosQueryRequest:
    def __init__(self, tipoAcesso: str, pagina: int = None):
        self.tipoAcesso = tipoAcesso
        self.pagina = pagina

    def __getitem__(self, key):
        return getattr(self, key)


@LoggerInterceptor()
class BuscarUsuariosQuery:
    def __init__(self, usuario_repository: UserRepositoryInteface):
        self.usuario_repository = usuario_repository

    async def execute(self, request: BuscarUsuariosQueryRequest) -> dict:
        try:
            usuarios = []
            if request["pagina"] == 0:
                usuario = self.usuario_repository.buscarTodosPorTipo(request["tipoAcesso"])
                for i in usuario:
                    usuarios.append(i.toDto())
                return usuarios
            buscarNumeroPaginas = self.usuario_repository.buscarNumeroDePaginas(request["tipoAcesso"] if request["tipoAcesso"] else None)
            if(request["tipoAcesso"] == None):
                usuario = self.usuario_repository.buscarTodos(request["pagina"])
                for i in usuario:
                    usuarios.append(i.toDto())
                return {"usuarios": usuarios, "numeroPaginas": buscarNumeroPaginas}
            
            usuario = self.usuario_repository.buscarPorTipoAcesso(request["tipoAcesso"], request["pagina"])

            for i in usuario:
                usuarios.append(i.toDto())

            return {"usuarios": usuarios, "numeroPaginas": buscarNumeroPaginas}
        except Exception as e:
            raise e
