from interceptors.LoggerInterceptor import LoggerInterceptor
from ...domain.repositories.UsuarioRepository import UserRepositoryInteface
from datetime import datetime
from ...domain.Usuario import Sexo

class AtualizarUsuarioUseCaseRequest:
    def __init__(self, tipoAcesso: str, nome: str, email: str, senha: str, dataNascimento: datetime, sexo: Sexo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.dataNascimento = dataNascimento
        self.sexo = sexo
        self.tipoAcesso = tipoAcesso

    def __getitem__(self, key):
        return getattr(self, key)

    
@LoggerInterceptor()
class AtualizarUsuarioUseCase:
    def __init__(self, usuario_repository: UserRepositoryInteface):
        self.usuario_repository = usuario_repository

    async def execute(self, request: AtualizarUsuarioUseCaseRequest) -> str:
        try:
            if request["tipoAcesso"] != "ADMIN":
                raise ValueError("Somente administradores podem atualizar usuários")
            
            usuario = self.usuario_repository.find(request["ra"])

            if(usuario == None):
                raise ValueError("Usuário não encontrado")
            
            usuario.atualizar_usuario(
                nome=request["nome"],
                email=request["email"],
                senha=request["senha"],
                dataNascimento=datetime.strptime(request["dataNascimento"], "%d-%m-%Y").date(),
                sexo=Sexo[request["sexo"]],
            )

            self.usuario_repository.update(usuario)


            return f"Usuário ra: {request['ra']} atualizado com sucesso!"
        except Exception as e:
            raise e
