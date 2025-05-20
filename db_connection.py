#Aqui se va a cargar la base de datos
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Configuración de la conexión a la base de datos
def get_connection():
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if conexion.is_connected():
            print("✅ Conexión exitosa a la base de datos")
            return conexion
    except Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")
        return None

# Configuración de SQLAlchemy para la conexión a la base de datos
def get_engine():
    engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")
    return engine

# PROVISIONAL= Verifica si se está conectando a la base de datos SE BORRA AL FINALIZAR
if __name__ == "__main__":
    # Conectar a la base de datos
    conexion = get_connection()
    engine = get_engine()

    if engine:
        print("✅ Conexión exitosa a la base de datos con SQLAlchemy")
        
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