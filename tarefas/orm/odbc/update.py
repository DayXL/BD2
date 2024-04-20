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
    
    sql_update = """
    UPDATE projeto
    SET responsavel = 2 
    WHERE codigo = 1;
    """
    cursor.execute(sql_update)

    conn.commit()
    print("Líder do projeto atualizado com sucesso!")
    
except pyodbc.Error as ex:
    print(f"Erro ao conectar ou executar comandos SQL: {ex}")
    
finally:
    if conn:
        conn.close()
