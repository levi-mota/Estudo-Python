nome_empresa = input("Qual o nome da empresa: ")
faturamento_mensal = float(input("Qual o seu faturamento mensal: "))
aliquota = float(0.10)
faturamento_aliquota = faturamento_mensal * aliquota
if faturamento_mensal <= 5000.00:
    print(f"Valor de imposto a pagar para a empresa {nome_empresa} é igual a R$ 00,00")
elif faturamento_mensal > 5000.00:
    print(f"Valor de imposto a pagar para a empresa {nome_empresa} é igual a R$ {faturamento_aliquota:.2f}")
else:
    print("Não foi possivel calcular")
    
    