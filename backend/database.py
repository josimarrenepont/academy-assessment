import os

import pandas as pd


def carregar_dados():
    if os.path.exists('alunos_db.xlsx'):
        alunos_db = pd.read_excel('alunos_db.xlsx').to_dict(orient='records')
    else:
        alunos_db = []

    if os.path.exists('avaliacoes_db.xlsx'):
        avaliacoes_db = pd.read_excel('avaliacoes_db.xlsx').to_dict(orient='records')
    else:
        avaliacoes_db = []

    return alunos_db, avaliacoes_db


def salvar_dados(alunos_db, avaliacoes_db):
    pd.DataFrame(alunos_db).to_excel('alunos_db.xlsx', index=False)
    pd.DataFrame(avaliacoes_db).to_excel('avaliacoes_db.xlsx', index=False)


alunos_db, avaliacoes_db = carregar_dados()
