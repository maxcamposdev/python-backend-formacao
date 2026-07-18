# Módulo de relatório de clientes (Dia 2 - Semana 3)
# Este arquivo é um MÓDULO: guarda funções reutilizáveis.

print("DEBUG __name__ =", __name__)

def contar_clientes(lista):
    total = len(lista)
    return total


def contar_ativos(lista):
    total_ativos = 0
    for cliente in lista:
        if cliente["situacao"] == "ativo":
            total_ativos = total_ativos + 1
    return total_ativos


def contar_segmento(lista, segmento):
    total = 0
    for cliente in lista:
        if cliente["segmento"] == segmento:
            total = total + 1
    return total


def contar_ativos_segmento(lista, segmento):
    total = 0
    for cliente in lista:
        if cliente["segmento"] == segmento and cliente["situacao"] == "ativo":
            total = total + 1
    return total


def contar_inativos(lista):
    total = 0
    for cliente in lista:
        if cliente["situacao"] == "inativo":
            total = total + 1
    return total


# TESTE: roda SÓ se o arquivo for executado diretamente.
# Se for importado por outro arquivo, este bloco NÃO executa.
if __name__ == "__main__":
    clientes = [
        {"nome": "mercado central", "segmento": "alimentacao", "situacao": "ativo"},
        {"nome": "oficina progresso", "segmento": "automotivo", "situacao": "ativo"},
        {"nome": "farmacia vida", "segmento": "saude", "situacao": "inativo"},
    ]
    print("Total de clientes:", contar_clientes(clientes))
    print("Clientes ativos:", contar_ativos(clientes))
    print("Clientes do segmento alimentacao:", contar_segmento(clientes, "alimentacao"))
    print("Clientes do segmento saude:", contar_segmento(clientes, "saude"))
    print("Ativos do segmento alimentacao:", contar_ativos_segmento(clientes, "alimentacao"))
    print("Clientes inativos:", contar_inativos(clientes))