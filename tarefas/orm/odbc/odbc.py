import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

server = os.getenv('SERVER')
port = os.getenv('PORT')
database = os.getenv('DATABASE')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

try:
    conn = pyodbc.connect(
        driver='{PostgreSQL Unicode}',
        server=server,
        port=port,
        database=database,
        uid=username,
        pwd=password
    )
    
    cursor = conn.cursor()
    print("Conexão bem-sucedida!")
    
except pyodbc.Error as ex:
    print(f"Erro ao conectar: {ex}")
    
finally:
    if conn:
        conn.close()
