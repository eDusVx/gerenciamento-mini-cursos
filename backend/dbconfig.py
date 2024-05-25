import mysql.connector
import os


class Database:
    __connection = None

    @staticmethod
    def conectar_mysql():
        if Database.__connection is None:
            Database.__connection = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_DATABASE"),
            )

    @staticmethod
    def obter_conexao():
        if Database.__connection is None:
            Database.conectar_mysql()
        return Database.__connection
