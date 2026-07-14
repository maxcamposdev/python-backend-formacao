print("=== Validador completo - CampOne ===")

nome = input("Nome da empresa: ").strip()
faturamento = float(input("Faturamento mensal (R$): "))
status = input("Status (ativa/inativa): ").strip()

print("\n--- Resultado ---")

# if nome and faturamento >= 5000 and status == "ativa":

if nome and faturamento >= 15000 and status == "ativa":
    print("✅ Cadastro válido!")
    print(f"Empresa: {nome}")
    print(f"Faturamento: R$ {faturamento:,.2f}")
    print(f"Status: {status}")
else:
    print("❌ Cadastro inválido.")
    print("Regras: nome preenchido, faturamento >= 5000 e status == ativa.")
