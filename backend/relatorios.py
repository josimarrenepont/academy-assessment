import pandas as pd


def gerar_relatorio():
    df_alunos = pd.DataFrame(alunos_db)
    df_avaliacoes = pd.DataFrame(avaliacoes_db)
    df_alunos.to_csv('relatorio_alunos.csv', index=False)
    df_avaliacoes.to_csv('relatorio_avaliacoes.csv', index=False)


#graficos.py
import matplotlib.pyplot as plt
import pandas as pd


def gerar_graficos():
    df_alunos = pd.DataFrame(alunos_db)
    df_avaliacoes = pd.DataFrame(avaliacoes_db)
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    df_alunos['idade'].hist()
    plt.title('Distribuição de Idades')
    
    plt.subplot(1, 2, 2)
    df_avaliacoes['imc'].hist()
    plt.title('Distribuição de IMC')
    
    plt.tight_layout()
    plt.savefig('graficos.png')
