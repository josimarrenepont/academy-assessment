from backend.database import carregar_dados, salvar_dados

# Carregar dados iniciais
alunos_db, avaliacoes_db = carregar_dados()

def cadastrar_aluno(nome, idade, peso, altura):
    aluno = {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura
    }
    alunos_db.append(aluno)
    salvar_dados(alunos_db, avaliacoes_db)

def registrar_avaliacao(nome, percentual_gordura, imc):
    avaliacao = {
        "nome": nome,
        "percentual_gordura": percentual_gordura,
        "imc": imc
    }
    avaliacoes_db.append(avaliacao)
    salvar_dados(alunos_db, avaliacoes_db)
