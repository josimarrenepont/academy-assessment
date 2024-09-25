import matplotlib.pyplot as plt
import pandas as pd

from backend.database import carregar_dados


def gerar_graficos():
    
    alunos_db, avaliacoes_db = carregar_dados()

    
    idades = [aluno['idade'] for aluno in alunos_db]

    
    plt.figure(figsize=(10, 6))

    
    n, bins, patches = plt.hist(idades, bins=10, color='skyblue', edgecolor='black', alpha=0.7)

    
    plt.title('Distribuição das Idades dos Alunos', fontsize=16, fontweight='bold')
    plt.xlabel('Idade', fontsize=14)
    plt.ylabel('Número de Alunos', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    
    plt.grid(axis='y', alpha=0.75)

    
    for count, x in zip(n, bins):
    
        plt.text(x, count, str(int(count)), ha='center', va='bottom', fontsize=10)

    
    plt.tight_layout() 
    plt.show()
