import requests

class BaseService:
    def __init__(self, api_url, token=None):
        self.api_url = api_url
        self.token = token

    def get(self, endpoint, **kwargs):
        return self.make_request('GET', f"{self.api_url}/core/{endpoint}", **kwargs)

    def post(self, endpoint, **kwargs):
        return self.make_request('POST', f"{self.api_url}/core/{endpoint}", **kwargs)

    def put(self, endpoint, **kwargs):
        return self.make_request('PUT', f"{self.api_url}/core/{endpoint}", **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.make_request('DELETE', f"{self.api_url}/core/{endpoint}", **kwargs)

    def add_token_to_headers(self, headers):
        if self.token:
            headers['Authorization'] = f'Bearer {self.token}'
        return headers

    def make_request(self, method, url, **kwargs):
        headers = kwargs.pop('headers', {})
        headers = self.add_token_to_headers(headers)
        response = requests.request(method, url, headers=headers, **kwargs)
        response.raise_for_status()
        return response.json()
