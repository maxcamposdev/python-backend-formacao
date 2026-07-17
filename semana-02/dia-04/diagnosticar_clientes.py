clientes = [
    {"nome": "oficina mecanica", "segmento": "automotivo", "situacao": "ativo"},
    {"nome": "petshop amigo", "segmento": "animais", "situacao": "ativo"},
    {"nome": "farmacia popular", "segmento": "saude", "situacao": "inativo"},
    {"nome": "academia fit", "segmento": "saude", "situacao": "ativo"}
]

total_saude = 0
total_ativos = 0

for cliente in clientes:
    if cliente["segmento"] == "saude":
        total_saude = total_saude + 1
    if cliente["situacao"] == "ativo":
        total_ativos = total_ativos + 1

print("Clientes do segmento saude:", total_saude)
print("Clientes ativos:", total_ativos)
print("Total de clientes:", len(clientes))