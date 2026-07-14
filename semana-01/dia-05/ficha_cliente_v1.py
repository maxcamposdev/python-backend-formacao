# ==============================
# FICHA DE CLIENTE v1 - CampOne
# ==============================

print("=== Ficha de Cliente - CampOne v1 ===\n")

# ------------------------------
# 1. ENTRADA DE DADOS
# ------------------------------

nome = input("Nome completo do cliente: ").strip()
email = input("E-mail do cliente: ").strip()
telefone = input("Telefone do cliente: ").strip()
status = input("Status (ativo/inativo): ").strip()
valor_contrato = float(input("Valor do contrato mensal (R$): "))

# ------------------------------
# 2. VALIDAÇÃO
# ------------------------------

if nome and valor_contrato >= 500 and status == "ativo":
    resultado = "✅ Cadastro válido"
else:
    resultado = "❌ Cadastro inválido"

# ------------------------------
# 3. EXIBIÇÃO DO RESULTADO
# ------------------------------

print("\n--- Resultado da Ficha ---")
print(f"Nome: {nome}")
print(f"E-mail: {email}")
print(f"Telefone: {telefone}")
print(f"Status: {status}")
print(f"Valor do Contrato: R$ {valor_contrato:,.2f}")
print(f"\n{resultado}")

# ------------------------------
# 4. MENSAGEM FINAL
# ------------------------------

print("\nObrigado por utilizar o sistema CampOne!")
print("Ficha de Cliente v1 - Semana 1, Dia 5")
