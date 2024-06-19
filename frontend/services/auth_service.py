from services.base_service import BaseService

class AuthService(BaseService):
    def login(self, email, senha):
        data = {
            "email": email,
            "senha": senha
        }

        return self.make_request('POST', f"{self.api_url}auth/login", json=data)