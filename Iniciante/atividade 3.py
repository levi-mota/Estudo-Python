nome_empresa = input("Qual o nome da empresa: ")
faturamento_mensal = float(input("Qual o seu faturamento mensal: "))
if faturamento_mensal <= 5000.00: aliquota = 00.00
elif faturamento_mensal <= 10000.00: aliquota = 00.05
elif faturamento_mensal > 10000.00: aliquota = 00.10
else:
    print("Nenhum valor a mostrar")
valor_final = faturamento_mensal * aliquota
print(f"Valor de imporsto a pagar para a empresa {nome_empresa} é R$ {valor_final:.2f}")