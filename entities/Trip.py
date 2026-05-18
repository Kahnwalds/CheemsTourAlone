from persistences.db import get_connection


class Trip:
    """
    Entidad que representa un viaje (trip).
    Contiene los métodos para interactuar con la base de datos.
    """

    def __init__(self, name: str, city: str, latitude: float, longitude: float):
        self.name = name
        self.city = city
        self.latitude = latitude
        self.longitude = longitude

    # ──────────────────────────────────────────────
    # READ — obtener todos los trips
    # ──────────────────────────────────────────────
    @staticmethod
    def get_all():
        connection = None
        cursor = None
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT id, name, city, latitude, longitude FROM trip")
            return cursor.fetchall()
        except Exception as ex:
            print(f"[ERROR] Trip.get_all: {ex}")
            return None
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    # ──────────────────────────────────────────────
    # CREATE — guardar un nuevo trip
    # ──────────────────────────────────────────────
    def save(self):
        connection = None
        cursor = None
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            sql = "INSERT INTO trip (name, city, latitude, longitude) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (self.name, self.city, self.latitude, self.longitude))
            connection.commit()
            return cursor.lastrowid
        except Exception as ex:
            print(f"[ERROR] Trip.save: {ex}")
            return None
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    # ──────────────────────────────────────────────
    # UPDATE — actualizar un trip existente por ID
    # ──────────────────────────────────────────────
    def update(self, trip_id: int) -> bool:
        connection = None
        cursor = None
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            sql = """
                UPDATE trip
                SET name = %s, city = %s, latitude = %s, longitude = %s
                WHERE id = %s
            """
            cursor.execute(sql, (self.name, self.city, self.latitude, self.longitude, trip_id))
            connection.commit()
            # rowcount > 0 significa que se actualizó al menos una fila
            return cursor.rowcount > 0
        except Exception as ex:
            print(f"[ERROR] Trip.update (id={trip_id}): {ex}")
            return False
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    # ──────────────────────────────────────────────
    # DELETE — eliminar un trip por ID
    # ──────────────────────────────────────────────
    @staticmethod
    def delete(trip_id: int) -> bool:
        connection = None
        cursor = None
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("DELETE FROM trip WHERE id = %s", (trip_id,))
            connection.commit()
            return cursor.rowcount > 0
        except Exception as ex:
            print(f"[ERROR] Trip.delete (id={trip_id}): {ex}")
            return False
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
