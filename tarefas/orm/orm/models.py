from pony.orm import *
from datetime import date
from dotenv import load_dotenv
import os

load_dotenv()

server = os.getenv('SERVER')
database = os.getenv('DATABASE')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

db = Database()

db.bind(provider='postgres', user=username, password=password, host=server, database=database)

class Funcionario(db.Entity):
    codigo = PrimaryKey(int, auto=True)
    nome = Required(str, max_len=150)
    sexo = Required(str, max_len=1)
    dt_nasc = Required(date)
    salario = Required(str)
    
    #Supervisor do funcionario
    supervisor = Required('Funcionario', reverse = 'funcionario')
    
    #Criando relação entre funcionario e supervisor
    funcionario = Set('Funcionario', reverse = 'supervisor')
    
    #Departamento que o funcionario faz parte
    depto = Required('Departamento', reverse = 'depto_cod')
    
    #Criando relação entre departamento e seu gerente
    func_ger = Set('Departamento', reverse = 'gerente')
    
    #Criando relação entre
    func_res = Set('Projeto', reverse = 'responsavel')
    
class Departamento(db.Entity):
    codigo = PrimaryKey(int, auto=True)
    nome = Optional(str, max_len=150)
    sigla = Required(str, max_len=10)
    descricao = Required(str, max_len=256)
    
    #Gerente do departamento
    gerente = Required('Funcionario', reverse = 'func_ger')
    
    # Criando relação entre funcionario e departamento
    depto_cod = Set('Funcionario', reverse = 'depto')
    
    
    # Criando relação entre projeto e departamento responsavel
    dep_resp = Set('Projeto', reverse = 'depto')

class Projeto(db.Entity):
    codigo = PrimaryKey(int, auto=True)
    nome = Required(str, max_len=150)
    descricao = Required(str, max_len=256)
    
    #Responsavel
    responsavel = Required('Funcionario', reverse = 'func_res')
    
    #depto
    depto = Required('Departamento', reverse = 'dep_resp')
    
    data_inicio = Required(date)
    data_fim = Required(date)
    
    # Criado relação entre atividade e o projeto que faz parte
    proj_resp = Set('Atividade', reverse = 'projeto')

class Atividade(db.Entity):
    codigo = PrimaryKey(int, auto=True)
    descricao = Required(str, max_len=256)
    
    #projeto
    projeto = Required('Projeto', reverse = 'proj_resp')
    
    data_inicio = Required(date)
    data_fim = Required(date)

db.generate_mapping()
