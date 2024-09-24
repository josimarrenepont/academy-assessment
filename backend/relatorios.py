import pandas as pd

from backend.database import carregar_dados


def gerar_relatorio():
    alunos_db, avaliacoes_db = carregar_dados()
    df_alunos = pd.DataFrame(alunos_db)
    df_avaliacoes = pd.DataFrame(avaliacoes_db)
    
    df_alunos.to_csv('relatorio_alunos.csv', index=False)
    df_avaliacoes.to_csv('relatorio_avaliacoes.csv', index=False)
