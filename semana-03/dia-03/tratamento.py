# Tratamento de erros (Dia 3 - Semana 3)
# Objetivo: capturar erro sem travar o programa.


def converter_numero(texto):
    try:
        numero = int(texto)
        return numero
    except ValueError:
        print("Erro: não consegui converter", texto, "para número.")
        return None


print(converter_numero("10"))
print(converter_numero("abc"))
print(converter_numero("42"))