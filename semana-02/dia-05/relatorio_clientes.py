clientes = [
    {"nome": "mercado central", "segmento": "alimentacao", "situacao": "ativo"},
    {"nome": "oficina progresso", "segmento": "automotivo", "situacao": "ativo"},
    {"nome": "farmacia vida", "segmento": "saude", "situacao": "inativo"},
    {"nome": "restaurante sabor", "segmento": "alimentacao", "situacao": "ativo"},
    {"nome": "clinica bem estar", "segmento": "saude", "situacao": "ativo"},
    {"nome": "padaria bairro", "segmento": "alimentacao", "situacao": "inativo"}
]

total_ativos = 0
total_inativos = 0
total_alimentacao = 0
total_alimentacao_ativos = 0

print("Clientes ativos cadastrados")

for cliente in clientes:
    if cliente["situacao"] == "ativo":
        total_ativos = total_ativos + 1
        print("-", cliente["nome"])

    if cliente["situacao"] == "inativo":
        total_inativos = total_inativos + 1

    if cliente["segmento"] == "alimentacao":
        total_alimentacao = total_alimentacao + 1

    if cliente["segmento"] == "alimentacao" and cliente["situacao"] == "ativo":
        total_alimentacao_ativos = total_alimentacao_ativos + 1

print("=== RELATORIO DE CLIENTES ===")
print("Total de clientes:", len(clientes))
print("Clientes ativos:", total_ativos)
print("Clientes inativos:", total_inativos)
print("Clientes do segmento alimentacao:", total_alimentacao)
print("Clientes ativos do segmento alimentacao:", total_alimentacao_ativos)