# Experimentação: relatório robusto (Dia 3 - Semana 3)
# Processa clientes mesmo quando algum dado está ausente ou inválido.


def idade_valida(cliente):
    try:
        idade = int(cliente["idade"])
        return idade
    except KeyError:
        return None   # cliente sem a chave "idade"
    except ValueError:
        return None   # valor não numérico


clientes = [
    {"nome": "mercado central", "idade": "30"},
    {"nome": "oficina progresso"},             # sem idade
    {"nome": "farmacia vida", "idade": "abc"}, # inválida
    {"nome": "padaria pao quente", "idade": "45"},
]

for cliente in clientes:
    idade = idade_valida(cliente)
    if idade is None:
        print(cliente["nome"], "-> idade não informada/inválida")
    else:
        print(cliente["nome"], "-> idade", idade)