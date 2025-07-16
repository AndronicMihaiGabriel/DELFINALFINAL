import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()


def get_connection():
    conn_str = (

        f"DRIVER={os.getenv('DRIVER')};"
        f"SERVER={os.getenv('SERVER')};"
        f"DATABASE={os.getenv('DATABASE')};"
        f"UID={os.getenv('UID')};"
        f"PWD={os.getenv('PWD')};"
        f"Encrypt={os.getenv('Encrypt')};"
        f"TrustServerCertificate={os.getenv('TrustServerCertificate')};"
        f"Connection Timeout={os.getenv('Connection_Timeout')};"
    )

    return pyodbc.connect(conn_str)
