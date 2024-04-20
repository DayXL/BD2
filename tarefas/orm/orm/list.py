from pony.orm import *
from models import Projeto

with db_session:
    projetos = Projeto.select()
    
    for projeto in projetos:
        print(f"Atividades do projeto {projeto.nome}:")

        for atividade in projeto.proj_resp:
            print(f"- {atividade.descricao}")

        print() 