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
print("✅ Conexión exitosa a PostgreSQL")

# Ejecuta una consulta de prueba
cursor.execute("SELECT version();")
version = cursor.fetchone()
print("Versión de PostgreSQL:", version)

# (Opcional) listar tablas existentes
cursor.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public';
""")

tablas = cursor.fetchall()
print("📋 Tablas actuales:")
for t in tablas:
    print("  -", t[0])

# Cierra conexión
cursor.close()
conexion.close()
