# backend/graficos.py
import matplotlib.pyplot as plt
import pandas as pd

from backend.database import carregar_dados


def gerar_graficos():
    # Carregar os dados dos alunos e avaliações
    alunos_db, avaliacoes_db = carregar_dados()

    # Exemplo de gráfico de idades
    idades = [aluno['idade'] for aluno in alunos_db]
    
    plt.hist(idades, bins=10, edgecolor='black')
    plt.title('Distribuição das Idades dos Alunos')
    plt.xlabel('Idade')
    plt.ylabel('Número de Alunos')
    plt.show()
