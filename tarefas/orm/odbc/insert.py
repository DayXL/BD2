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
    
    insert = """
    INSERT INTO atividade (descricao, projeto, data_inicio, data_fim)
    VALUES ('Nova atividade 3', 2, '2024-04-25', '2024-04-30')
    """

    cursor.execute(insert)

    conn.commit()
    print("Atividade inserida com sucesso!")
    
except pyodbc.Error as ex:
    print(f"Erro ao conectar ou executar comandos SQL: {ex}")
    
finally:
    if conn:
        conn.close()
