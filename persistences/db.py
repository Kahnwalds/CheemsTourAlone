import os
import mysql.connector


def get_connection():
    """
    Crea y retorna una conexión a la base de datos MySQL.
    Los datos de conexión se leen desde variables de entorno
    para no exponer credenciales en el código fuente.
    """
    try:
        db_host = os.environ.get('DB_HOST')
        db_user = os.environ.get('DB_USER', 'avnadmin')
        db_pw   = os.environ.get('DB_PW')
        db_port = os.environ.get('DB_PORT', '10667')
        db_name = os.environ.get('DB_NAME', 'defaultdb')

        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pw,
            database=db_name,
            port=int(db_port)
        )
        return conn

    except Exception as ex:
        print(f"[ERROR] get_connection: {ex}")
        return None
