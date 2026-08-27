empresa = input("Qual o nome da empresa? ")
faturamento_mes = float(input("Qual seu faturamento mensal? "))
if faturamento_mes <= 5000.00: aliquota = 0
elif faturamento_mes < 10000.00: aliquota = 0.05
elif faturamento_mes >= 10000.00: aliquota = 0.10
calculo_iss = faturamento_mes * aliquota
print(f"A empresa {empresa} deve pagar de iss o valor de R$ {calculo_iss:.2f}") 
    
continuar = input("Deseja continuar? s/n: ")

while continuar == "s": 
    empresa = input("Qual o nome da empresa? ")
    faturamento_mes = float(input("Qual seu faturamento mensal? "))
    if faturamento_mes <= 5000.00: aliquota = 0
    elif faturamento_mes < 10000.00: aliquota = 0.05
    elif faturamento_mes >= 10000.00: aliquota = 0.10
    calculo_iss = faturamento_mes * aliquota
    print(f"A empresa {empresa} deve pagar de iss o valor de R$ {calculo_iss:.2f}") 
    continuar = input("Deseja continuar? s/n: ")

print("Programa finalizado!")