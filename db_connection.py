#Aqui se va a cargar la base de datos
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la conexión a la base de datos
def get_connection():
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if conexion.is_connected():
            print("✅ Conexión exitosa a la base de datos")
            return conexion
    except Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")
        return None
    
# PROVISIONAL= Verifica si se está conectando a la base de datos SE BORRA AL FINALIZAR
if __name__ == "__main__":
    # Conectar a la base de datos
    conexion = get_connection()

    # Verificar si la conexión fue exitosa
    if conexion:
        # Crear un cursor para ejecutar consultas
        cursor = conexion.cursor()

        # Ejecutar una consulta de prueba
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        print(f"Conectado a la base de datos: {db_name[0]}")

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()