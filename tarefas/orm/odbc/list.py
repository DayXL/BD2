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
    
    cursor.execute("SELECT * FROM projeto;")
    projetos = cursor.fetchall()    
    
    for projeto in projetos:
        print(f"Atividades do projeto {projeto[1]}:")
        
        cursor.execute(f"SELECT * FROM atividade WHERE projeto = {projeto[0]};")
        atividades = cursor.fetchall()

        for atividade in atividades:
            print(f"{atividade[1]}")
        
        print()
    
except pyodbc.Error as ex:
    print(f"Erro ao conectar ou executar comandos SQL: {ex}")
    
finally:
    if conn:
        conn.close()
