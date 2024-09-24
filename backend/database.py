import os

import pandas as pd

# Define o caminho da pasta 'data'
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def carregar_dados():
    alunos_path = os.path.join(DATA_DIR, 'alunos_db.csv')
    avaliacoes_path = os.path.join(DATA_DIR, 'avaliacoes_db.csv')

    if os.path.exists(alunos_path):
        alunos_db = pd.read_csv(alunos_path, sep=';').to_dict(orient='records')
    else:
        alunos_db = []

    if os.path.exists(avaliacoes_path):
        avaliacoes_db = pd.read_csv(avaliacoes_path, sep=';').to_dict(orient='records')
    else:
        avaliacoes_db = []

    return alunos_db, avaliacoes_db

def salvar_dados(alunos_db, avaliacoes_db):
    alunos_path = os.path.join(DATA_DIR, 'alunos_db.csv')
    avaliacoes_path = os.path.join(DATA_DIR, 'avaliacoes_db.csv')

    pd.DataFrame(alunos_db).to_csv(alunos_path, index=False, sep=';')
    pd.DataFrame(avaliacoes_db).to_csv(avaliacoes_path, index=False, sep=';')
