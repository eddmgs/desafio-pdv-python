#DESAFIO 1 - PDV SIMPLES

#1. PREPARAÇÃO INICIAL
# Lista que vai guardar o histórico de todas as compras do dia.
# Cada compra será salva como uma sub-lista: [valor original, desconto, valor final]

historico = []

valor = float(input("Valor da compra (0 para encerrar): R$ "))

# 2. LOOP PRINCIPAL (uma volta = uma compra)
# Continua processando compras até o usuário digitar 0.

while valor < 0:
    print("Valor inválido. Por favor, insira um valor válido.")
    valor = float(input("Valor da compra (0 para encerrar): R$ "))

# Pede a idade do comprador que nao pode ser negativa

while valor != 0:
    valor_idade = int(input("Idade do comprador: "))

    while valor_idade < 0:
        print("Idade inválida. Por favor, insira uma idade válida.")
        valor_idade = int(input("Idade do comprador: "))

    desconto = 0
    valor_final = valor

# REGRA 1: compradores com 65 anos ou mais ganham 20% de desconto

    if valor_idade >= 65:
        desconto = valor * 0.20
        valor_final = valor - desconto

 # REGRA 2: se o valor já com o primeiro desconto passar de R$ 100,
# ganha mais 10% de desconto extra (aplicado sobre o valor atual).

    if valor_final > 100:
        desconto_extra = valor_final * 0.10
        desconto += desconto_extra
        valor_final -= desconto_extra

 # Guarda os dados desta compra no histórico para o resumo final

    historico.append([valor, desconto, valor_final])

    print(f"Desconto total: R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")

    valor = float(input("Valor da próxima compra (0 para encerrar): R$ "))

    while valor < 0:
        print("Valor inválido. Por favor, insira um valor válido.")
        valor = float(input("Valor da próxima compra (0 para encerrar): R$ "))

quantidade_compras = len(historico)

# 3. CÁLCULO DOS TOTAIS DO DIA

total_bruto = 0
desconto_total = 0
valor_final_total = 0

for compra in historico:
    total_bruto += compra[0]
    desconto_total += compra[1]
    valor_final_total += compra[2]
        
# 4. RESUMO FINAL

print("\n--- Resumo do dia ---")
print(f"Quantidade de compras: {quantidade_compras}")
print(f"Valor total bruto: R$ {total_bruto:.2f}")
print(f"Desconto total concedido: R$ {desconto_total:.2f}")
print(f"Valor total final: R$ {valor_final_total:.2f}")
print("Programa encerrado.")