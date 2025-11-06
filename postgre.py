import psycopg2

# Configura los datos de conexión
conexion = psycopg2.connect(
    host="localhost",
    port=5432,
    database="midb",
    user="user",
    password="password"
)

# Crea un cursor
cursor = conexion.cursor()

# Ejecuta una consulta de prueba
cursor.execute("SELECT version();")
version = cursor.fetchone()
print("Versión de PostgreSQL:", version)

# Cierra conexión
cursor.close()
conexion.close()
