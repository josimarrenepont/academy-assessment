import os

import matplotlib.pyplot as plt
import pandas as pd

# Define o diretório de dados
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

def gerar_graficos():
    # Carrega os dados dos alunos e avaliações
    alunos_db, avaliacoes_db = carregar_dados()

    # Extrai as idades dos alunos
    idades = [aluno['idade'] for aluno in alunos_db]

    # Cria uma nova figura para o gráfico
    plt.figure(figsize=(10, 6))

    # Gera o histograma das idades
    n, bins, patches = plt.hist(idades, bins=10, color='skyblue', edgecolor='black', alpha=0.7)

    # Configurações do gráfico
    plt.title('Distribuição das Idades dos Alunos', fontsize=16, fontweight='bold')
    plt.xlabel('Idade', fontsize=14)
    plt.ylabel('Número de Alunos', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', alpha=0.75)

    # Adiciona as contagens acima de cada barra do histograma
    for count, x in zip(n, bins):
        plt.text(x, count, str(int(count)), ha='center', va='bottom', fontsize=10)

    # Ajusta o layout e exibe o gráfico
    plt.tight_layout()

    # Salva o gráfico como imagem (opcional)
    plt.savefig('distribuicao_idades.png')  # Salva como 'distribuicao_idades.png'

    # Exibe o gráfico
    plt.show()

# Executa a função ao rodar o script
if __name__ == "__main__":
    gerar_graficos()
