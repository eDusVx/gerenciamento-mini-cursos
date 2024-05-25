from flask import Flask
from dotenv import load_dotenv
from modules.auth.AuthController import auth_controller
from modules.core.CoreController import coreController
from dbconfig import Database
import os
from colorama import Fore
from flask_jwt_extended import JWTManager


def create_app():
    load_dotenv()
    app = Flask(os.getenv("APP_NAME"))
    app.config.from_prefixed_env()
    app.register_blueprint(auth_controller)
    app.register_blueprint(coreController)
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET")
    JWTManager(app)
    Database.conectar_mysql()
    return app


def listar_rotas(app):
    print(f"{Fore.LIGHTCYAN_EX}Rotas registradas:")
    for rule in app.url_map.iter_rules():
        for method in rule.methods:
            if method in ("GET", "POST", "PUT", "DELETE", "PATCH"):
                print(
                    f"{Fore.LIGHTBLUE_EX}{method}:{Fore.RESET} {Fore.GREEN}{rule}{Fore.RESET}"
                )


app = create_app()
listar_rotas(app)
