cliente = {
    "nome": "barbearia max campos",
    "segmento": "saude e beleza",
    "situacao": "ativo"
}

cliente["situacao"] = "inativo"
cliente["responsavel"] = "max campos"

print(cliente)
print(cliente["nome"])
print(cliente.get("responsavel", "responsavel não encontrado"))
