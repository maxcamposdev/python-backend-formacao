clientes = ["Mercado Central", "Barbearia Max Campos", "Clínica Vida", "Studio Bella"]

clientes.append("Pet Loja")
clientes[1] = "Studio Bella Premium"
clientes.remove("Clínica Vida")
clientes.pop(0)

print(clientes)
print(len(clientes))
print(clientes[0])
