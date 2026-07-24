def contar_ativos(clientes):
    total = 0
    for cliente in clientes:
        if cliente["ativo"]:
            total = total + 1
    return total