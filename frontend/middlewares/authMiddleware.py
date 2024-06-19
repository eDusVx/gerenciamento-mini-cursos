from flask import g, session, current_app
import requests

def authMiddleware():
    g.api_url = current_app.config['API_URL']
    g.token = session.get('token')

