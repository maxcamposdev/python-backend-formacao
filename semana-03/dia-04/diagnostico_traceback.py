def media(numeros):
    soma = 0
    for n in numeros:
        soma = soma + n
    return soma / len(numeros)

print(media([10, 20, 30]))