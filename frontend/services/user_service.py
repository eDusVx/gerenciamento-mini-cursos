import json
from services.base_service import BaseService

class UserService(BaseService):
    def __init__(self, api_url, token=None):
        super().__init__(api_url, token)
    
    def create_user(self, user_data):
        return self.make_request('POST', f"{self.api_url}/auth/registrar-usuario", json=user_data)
    
    def update_user(self, user_data):
        return self.put("atualizar-usuario", json=user_data)
    
    def delete_user(self, user_ra):
        return self.delete("remover-usuario", json={"ra": user_ra})

    def list_users(self, pageNumber, access_type):
        return self.get("buscar-usuarios", params={"pagina": pageNumber, "tipoAcesso": access_type})
