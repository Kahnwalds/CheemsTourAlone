import os
try:
    import mysql.connector
except ImportError:
    print("[WARNING] mysql.connector not installed. Install with: pip install mysql-connector-python")


def get_connection():

    try:
        db_host = os.environ.get('DB_HOST', 'localhost')
        db_user = os.environ.get('DB_USER', 'root')
        db_pw   = os.environ.get('DB_PW', '')
        db_port = os.environ.get('DB_PORT', '3306')
        db_name = os.environ.get('DB_NAME', 'cheemstouralone')

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