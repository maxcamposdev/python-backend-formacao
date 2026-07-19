# else e finally (Dia 3 - Semana 3)

def converter(texto):
    try:
        numero = int(texto)
    except ValueError:
        print("Falhou:", texto)
    else:
        print("Sucesso! número =", numero)
    finally:
        print("--- fim da tentativa ---")


converter("25")
converter("xyz")