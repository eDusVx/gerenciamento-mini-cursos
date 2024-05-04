from jwt import encode
from datetime import datetime, timedelta
from ...application.services.AuthService import AuthServiceInterface
from ...domain.Usuario import TipoAcesso
import os

class AuthService(AuthServiceInterface):
    def autenticar(self, cpf: str, nome:str, email:str, tipoAcesso: TipoAcesso) -> str:
        expira_em = datetime.now() + timedelta(hours=1) 
        payload = {"sub":"JWT_AUTENTICATION","cpf": cpf, "nome":nome, "email": email, "tipoAcesso": tipoAcesso.name, "exp": expira_em.strftime("%d-%m-%Y %H:%M:%S")}
        token = encode(payload, os.getenv('JWT_SECRET'))
        return token