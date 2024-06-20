from flask import redirect, url_for

def unauthorizedMiddleware(response):
        if response.status_code == 401:
            return redirect(url_for('login'))
        return response

