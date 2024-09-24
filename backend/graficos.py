import matplotlib.pyplot as plt
import pandas as pd

from backend.database import carregar_dados


def gerar_graficos():
    alunos_db, avaliacoes_db = carregar_dados()
    
    # Criar gráficos com os dados (exemplo)
    # Suponha que você queira plotar a idade dos alunos
    idades = [aluno['idade'] for aluno in alunos_db]
    
    plt.hist(idades, bins=10, edgecolor='black')
    plt.title('Distribuição das Idades dos Alunos')
    plt.xlabel('Idade')
    plt.ylabel('Número de Alunos')
    plt.show()
