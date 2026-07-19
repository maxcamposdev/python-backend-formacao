# Tratamento de erros específicos (Dia 3 - Semana 3)
# Capturar tipos diferentes de erro de forma separada.


def processar_cliente(cliente):
    try:
        nome = cliente["nome"]
        idade = int(cliente["idade"])
        print("OK:", nome, "- idade", idade)
    except KeyError as e:
        print("Faltou a chave:", e)
    except ValueError as e:
        print("Idade inválida:", e)


clientes = [
    {"nome": "mercado central", "idade": "30"},
    {"nome": "oficina progresso"},              # sem "idade" -> KeyError
    {"nome": "farmacia vida", "idade": "abc"},  # não numérico -> ValueError
]

for cliente in clientes:
    processar_cliente(cliente)