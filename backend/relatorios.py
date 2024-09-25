from datetime import datetime

import pandas as pd

from backend.database import carregar_dados


def gerar_relatorio():
    
    alunos_db, avaliacoes_db = carregar_dados()
    
    
    if not alunos_db or not avaliacoes_db:
        print("Erro: Dados não carregados corretamente.")
        return

    
    df_alunos = pd.DataFrame(alunos_db)
    df_avaliacoes = pd.DataFrame(avaliacoes_db)

    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    
    df_alunos.to_csv(f'relatorio_alunos_{timestamp}.csv', index=False)
    df_avaliacoes.to_csv(f'relatorio_avaliacoes_{timestamp}.csv', index=False)
    
    
    print(f"Relatório de Alunos gerado com {len(df_alunos)} registros.")
    print(f"Relatório de Avaliações gerado com {len(df_avaliacoes)} registros.")
    print("Relatórios gerados com sucesso!")
