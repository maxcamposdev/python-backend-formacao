# print("=== Cadastro de Empresa - CampOne ===")

# nome = input("Nome da empresa: ")
# segmento = input("Segmento de atuação: ")
# faturamento_str = input("Faturamento mensal (R$): ")

# print(f"\nEmpresa cadastrada com sucesso!")
# print(f"Nome: {nome}")
# print(f"Segmento: {segmento}")
# print(f"Faturamento: R$ {faturamento_str}")

#print("=== Cadastro de Empresa - CampOne ===")

# nome = input("Nome da empresa: ")
# segmento = input("Segmento de atuação: ")
# faturamento_str = input("Faturamento_str (R$): ")

# faturamento = float(faturamento_str)

# print(f"\nEmpresa cadastrada com sucesso!")
# print(f"Nome: {nome}")
# print(f"Segmento: {segmento}")
# print(f"Faturmamento: R$ {faturamento:.2f}")

# print("=== Validador de Cadastro Empresarial - CampOne ===")

# nome = input("Nome da empresa: ").strip()
# segmento = input("Segmento de atuação: ").strip()
# faturamento_str = input("Faturamento mensal (R$): ")

# faturamento = float(faturamento_str)

# print("\n--- Resultado da Validação ---")

# if nome and segmento and faturamento > 0:
#     print("✅ Cadastro válido!")
#     print(f"Empresa: {nome}")
#     print(f"Segmento: {segmento}")
#     print(f"Faturamento mensal: R$ {faturamento:,.2f}")
# else:
#     print("❌ Cadastro inválido. Verifique os dados informados.")

print("=== Validador de Cadastro Empresarial - CampOne ===")

nome = input("Nome da empresa: ").strip()
segmento = input("Segmento de atuação: ").strip()
faturamento_str = input("Faturamento mensal (R$): ")

faturamento = float(faturamento_str)

print("\n--- Resultado da Validação ---")

if not nome or not segmento:
    print("❌ Cadastro inválido. Nome e segmento são obrigatórios")
elif faturamento < 5000:
    print("❌ Cadastro inválido. Faturamento mínimo de R$ 5.000,00.")
else:
    print("✅ Cadastro válido!")
    print(f"Empresa: {nome}")
    print(f"Segmento: {segmento}")
    print(f"Faturamento mensal: R$ {faturamento:,.2f}")

    if faturamento >= 50000:
        print("Classificação: Emrpesa Premium")
    elif faturamento >= 10000:
        print("Classificação: Empresa Standard")
    else:
        print("Classificação: Empresa Inicial")
