import pandas as pd


def gerar_relatorio():
    df_alunos = pd.DataFrame(alunos_db)
    df_avaliacoes = pd.DataFrame(avaliacoes_db)
    df_alunos.to_csv('relatorio_alunos.csv', index=False)
    df_avaliacoes.to_csv('relatorio_avaliacoes.csv', index=False)
