import campone

clientes = [
    {"nome": "mercado central", "ativo": True},
    {"nome": "oficina progresso", "ativo": False},
    {"nome": "farmacia vida", "ativo": True},
]

print("Clientes ativos:", campone.contar_ativos(clientes))