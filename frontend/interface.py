import tkinter as tk
from tkinter import messagebox, ttk

from backend.graficos import gerar_graficos
from backend.main import (cadastrar_aluno, mostrar_dados_aluno,
                          registrar_avaliacao)
from backend.relatorios import gerar_relatorio


class Aplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro de Alunos")
        self.root.geometry("600x400")

        # Cadastro de Alunos
        self.frame_cadastro = ttk.LabelFrame(self.root, text="Cadastro de Alunos", padding=(10, 10))
        self.frame_cadastro.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(self.frame_cadastro, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        self.nome_entry = ttk.Entry(self.frame_cadastro)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame_cadastro, text="Idade:").grid(row=1, column=0, padx=5, pady=5)
        self.idade_entry = ttk.Entry(self.frame_cadastro)
        self.idade_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.frame_cadastro, text="Peso:").grid(row=2, column=0, padx=5, pady=5)
        self.peso_entry = ttk.Entry(self.frame_cadastro)
        self.peso_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.frame_cadastro, text="Altura:").grid(row=3, column=0, padx=5, pady=5)
        self.altura_entry = ttk.Entry(self.frame_cadastro)
        self.altura_entry.grid(row=3, column=1, padx=5, pady=5)

        self.cadastrar_btn = ttk.Button(self.frame_cadastro, text="Cadastrar Aluno", command=self.cadastrar_aluno)
        self.cadastrar_btn.grid(row=4, column=0, columnspan=2, pady=10)

        # Registro de Avaliações
        self.frame_avaliacao = ttk.LabelFrame(self.root, text="Registro de Avaliações", padding=(10, 10))
        self.frame_avaliacao.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(self.frame_avaliacao, text="Nome do Aluno:").grid(row=0, column=0, padx=5, pady=5)
        self.nome_avaliacao_entry = ttk.Entry(self.frame_avaliacao)
        self.nome_avaliacao_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame_avaliacao, text="Percentual de Gordura:").grid(row=1, column=0, padx=5, pady=5)
        self.percentual_gordura_entry = ttk.Entry(self.frame_avaliacao)
        self.percentual_gordura_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.frame_avaliacao, text="IMC:").grid(row=2, column=0, padx=5, pady=5)
        self.imc_entry = ttk.Entry(self.frame_avaliacao)
        self.imc_entry.grid(row=2, column=1, padx=5, pady=5)

        self.registrar_btn = ttk.Button(self.frame_avaliacao, text="Registrar Avaliação", command=self.registrar_avaliacao)
        self.registrar_btn.grid(row=3, column=0, columnspan=2, pady=10)

        # Exibir Dados
        self.frame_dados = ttk.LabelFrame(self.root, text="Exibir Dados do Aluno", padding=(10, 10))
        self.frame_dados.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(self.frame_dados, text="Nome do Aluno:").grid(row=0, column=0, padx=5, pady=5)
        self.nome_dados_entry = ttk.Entry(self.frame_dados)
        self.nome_dados_entry.grid(row=0, column=1, padx=5, pady=5)

        self.exibir_btn = ttk.Button(self.frame_dados, text="Exibir Dados", command=self.exibir_dados)
        self.exibir_btn.grid(row=1, column=0, columnspan=2, pady=10)

        # Relatórios e Gráficos
        self.frame_relatorios = ttk.LabelFrame(self.root, text="Relatórios e Gráficos", padding=(10, 10))
        self.frame_relatorios.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.relatorio_btn = ttk.Button(self.frame_relatorios, text="Gerar Relatório", command=self.gerar_relatorio)
        self.relatorio_btn.grid(row=0, column=0, padx=5, pady=5)

        self.graficos_btn = ttk.Button(self.frame_relatorios, text="Gerar Gráficos", command=self.gerar_graficos)
        self.graficos_btn.grid(row=0, column=1, padx=5, pady=5)

    def cadastrar_aluno(self):
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()
        peso = self.peso_entry.get()
        altura = self.altura_entry.get()

        if nome and idade and peso and altura:
            cadastrar_aluno(nome, int(idade), float(peso), float(altura))
            messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        else:
            messagebox.showwarning("Atencao", "Todos os campos devem ser preenchidos!")

    def registrar_avaliacao(self):
        nome = self.nome_avaliacao_entry.get()
        percentual_gordura = self.percentual_gordura_entry.get()
        imc = self.imc_entry.get()

        if nome and percentual_gordura and imc:
            registrar_avaliacao(nome, float(percentual_gordura), float(imc))
            messagebox.showinfo("Sucesso", "Avaliação registrada com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")

    def exibir_dados(self):
        nome = self.nome_dados_entry.get()
        if nome:
            dados, avaliacoes = mostrar_dados_aluno(nome)
            if dados:
                messagebox.showinfo("Dados do Aluno", f"Dados: {dados}\nAvaliações: {avaliacoes}")
            else:
                messagebox.showwarning("Atenção", "Aluno não encontrado!")
        else:
            messagebox.showwarning("Atenção", "Informe o nome do aluno!")

    def gerar_relatorio(self):
        gerar_relatorio()
        messagebox.showinfo("Sucesso", "Relatório gerado com sucesso!")

    def gerar_graficos(self):
        gerar_graficos()
        messagebox.showinfo("Sucesso", "Gráficos gerados com sucesso!")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()
