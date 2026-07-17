clientes = [
    {"nome": "logistica one", "segmento": "armazem", "situacao": "ativo"},
    {"nome": "perfumaria campos", "segmento": "saude e beleza", "situacao": "ativo"},
    {"nome": "mercado novo", "segmento": "alimentacao", "situacao": "ativo"},
    {"nome": "pet dog e cat", "segmento": "animais domesticos", "situacao": "ativo"}
]

total_ativos = 0
total_alimentacao = 0

for cliente in clientes:
    if cliente["situacao"] == "ativo":
        total_ativos = total_ativos + 1
    if cliente["segmento"] == "alimentacao":
        total_alimentacao = total_alimentacao + 1
print("Clientes do segmento alimentacao:", total_alimentacao)
print("Clientes ativos:", total_ativos)
print("Total de clientes:", len(clientes))
