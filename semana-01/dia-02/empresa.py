# Dados da empresa na plataforma CampOne
# Empresa 1

nome = "Tech Casa"
segmento = "Varejo de tecnologia"
ativa = True

# print("Nome:", nome, "| Tipo:", type(nome))
# print("Segmento:", segmento, "| Tipo:", type(segmento))
# print("Ativa:", ativa, "| Tipo:", type(ativa))

print(f"EMPRESA: {nome}")
print(f"Segmento: {segmento}")
print(f"Status ativa: {ativa}")
print(f"---")
print(f"Tipos: nome={type(nome).__name__}, segmento={type(segmento).__name__}, ativa={type(ativa).__name__}")

print(f"---")

# Empresa 2

nome2 = "Barbearia Max Campos"
segmento2 = "Beleza e Estética"
ativa2 = True
faturamento = 60.000
colaboradores = 4

print(f"EMPRESA: {nome2}")
print(f"Segmento: {segmento2}")
print(f"Ativa: {ativa2}")
print(f"Faturamento Mensal: R$ {faturamento}")
print(f"Colaboradores: {colaboradores}")
print(f"---")
print(f"Tipos: nome2={type(nome2).__name__}, segmento2={type(segmento2).__name__}, ativa2={type(ativa2).__name__}, faturamento={type(faturamento).__name__}, colaboradores={type(colaboradores).__name__}")
