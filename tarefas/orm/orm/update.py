from pony.orm import *
from models import Projeto, Funcionario

with db_session:
    projeto = Projeto[1]

    novo_resp = Funcionario[1]

    projeto.responsavel = novo_resp
    
    commit()
    