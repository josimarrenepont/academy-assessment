from backend.data.database import alunos_db, avaliacoes_db


def cadastrar_aluno(nome, idade, peso, altura):
    aluno = {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura
    }
    alunos_db.append(aluno)

def registrar_avaliacao(nome, percentual_gordura, imc):
    avaliacao = {
        "nome": nome,
        "percentual_gordura": percentual_gordura,
        "imc": imc
    }
    avaliacoes_db.append(avaliacao)

def mostrar_dados_aluno(nome):
    dados = [aluno for aluno in alunos_db if aluno["nome"] == nome]
    avaliacoes = [avaliacao for avaliacao in avaliacoes_db if avaliacao["nome"] == nome]
    return dados, avaliações
