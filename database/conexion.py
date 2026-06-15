
import psycopg2
import os

from dotenv import load_dostenv

class Conexion:
    @staticmethod

    def obtener_conexion():

        return psycopg2.connect(
            host=os.gatenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DV_PORT")
        )

