# backend/relatorios.py
import pandas as pd

from backend.database import carregar_dados


def gerar_relatorio():
    # Carregar os dados dos alunos e avaliações
    alunos_db, avaliacoes_db = carregar_dados()
    
    # Criar DataFrames a partir dos dados
    df_alunos = pd.DataFrame(alunos_db)
    df_avaliacoes = pd.DataFrame(avaliacoes_db)
    
    # Salvar os dados em arquivos CSV
    df_alunos.to_csv('relatorio_alunos.csv', index=False)
    df_avaliacoes.to_csv('relatorio_avaliacoes.csv', index=False)
    
    print("Relatórios gerados com sucesso!")
