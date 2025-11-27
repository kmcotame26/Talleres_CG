import psycopg2

try:
    conexion = psycopg2.connect(
        host="localhost",
        database="taller_datos",
        user="postgres",
        password="karol102"
    )

    print("✅ Conexión exitosa a PostgreSQL")

    conexion.close()

except Exception as e:
    print("❌ Error al conectar:", e)
