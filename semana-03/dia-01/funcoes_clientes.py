clientes = [
    {"nome": "mercado central", "segmento": "alimentacao", "situacao": "ativo"},
    {"nome": "oficina progresso", "segmento": "automotivo", "situacao": "ativo"},
    {"nome": "farmacia vida", "segmento": "saude", "situacao": "inativo"},
]

def contar_clientes(lista):
    total = len(lista)
    return total

resultado = contar_clientes(clientes)
print("Total de clientes:", resultado)

def contar_ativos(lista):
    total_ativos = 0
    for cliente in lista:
        if cliente["situacao"] == "ativo":
            total_ativos = total_ativos + 1
    return total_ativos

ativos = contar_ativos(clientes)
print("Clientes ativos:", ativos)

def contar_por_segmento(lista, segmento):
    total = 0
    for cliente in lista:
        if cliente["segmento"] == segmento:
            total = total + 1
    return total

alimentacao = contar_por_segmento(clientes, "alimentacao")
print("Clientes do segmento alimentacao:", alimentacao)

saude = contar_por_segmento(clientes, "saude")
print("Clientes do segmento saude:", saude)

def contar_ativos_por_segmento(lista, segmento):
    total = 0
    for cliente in lista:
        if cliente["segmento"] == segmento and cliente["situacao"] == "ativo":
            total = total + 1
    return total

ativos_alimentacao = contar_ativos_por_segmento(clientes, "alimentacao")
print("Ativos do segmento alimentacao:", ativos_alimentacao)

def contar_inativos(lista):
    total = 0
    for cliente in lista:
        if cliente["situacao"] == "inativo":
            total = total + 1
    return total

inativos = contar_inativos(clientes)
print("Clientes inativos:", inativos)
