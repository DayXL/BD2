from pony.orm import *
from datetime import date
from models import Projeto, Atividade

with db_session:
    projeto_existente = Projeto[1]

    nova_atividade = Atividade(
        descricao='Nova atividade 3',
        projeto=projeto_existente,
        data_inicio=date(2024, 4, 21),
        data_fim=date(2024, 4, 30)
    )
    commit()  
