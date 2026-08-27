print("Bem-vindo(a) ao sistema de cálculo de INSS")
nome_colaborador = input("Qual o nome do colaborador? ")
salario_colaborador = float(input("Qual o salário do colaborador? "))
continuar = input(f"Confirme os dados antes de continuar: Colaborador {nome_colaborador}, Salário {salario_colaborador:.2f}. Deseja continuar? s/n ")

while continuar == "n":
    nome_colaborador = input("Qual o nome do colaborador? ")
    salario_colaborador = float(input("Qual o salário do colaborador? "))
    continuar = input(f"Confirme os dados antes de continuar: Colaborador {nome_colaborador}, Salário {salario_colaborador:.2f}. Deseja continuar? s/n ")

if salario_colaborador <= 1621.00: aliquota = 0.075
elif salario_colaborador <= 2902.84: aliquota = 0.09
elif salario_colaborador <= 4354.27: aliquota = 0.12
else: aliquota = 0.14

if aliquota == 0.075: deducao = 0
elif aliquota == 0.09: deducao = 24.32
elif aliquota == 0.12: deducao = 111.40
else: deducao = 0

desconto = salario_colaborador * aliquota
desconto_final = desconto - deducao

print(f"O desconto bruto de Inss do colaborador {nome_colaborador} é de R$ {desconto:.2f} com uma dedução de R$ {deducao:.2f}. Com desconto liquido de R$ {desconto_final:.2f}.")

nova_rodada = input("Fazer novos calculos? s/n ")

while nova_rodada == "s":
    nome_colaborador = input("Qual o nome do colaborador? ")
    salario_colaborador = float(input("Qual o salário do colaborador? "))
    continuar = input(f"Confirme os dados antes de continuar: Colaborador {nome_colaborador}, Salário {salario_colaborador:.2f}. Deseja continuar? s/n ")
   
    if salario_colaborador <= 1621.00: aliquota = 0.075
    elif salario_colaborador <= 2902.84: aliquota = 0.09
    elif salario_colaborador <= 4354.27: aliquota = 0.12
    else: aliquota = 0.14

    if aliquota == 0.075: deducao = 0
    elif aliquota == 0.09: deducao = 24.32
    elif aliquota == 0.12: deducao = 111.40
    else: deducao = 0

    desconto = salario_colaborador * aliquota
    desconto_final = desconto - deducao

    print(f"O desconto bruto de Inss do colaborador {nome_colaborador} é de R$ {desconto:.2f} com uma dedução de R$ {deducao:.2f}. Com desconto liquido de R$ {desconto_final:.2f}.")
    nova_rodada = input("Fazer novos calculos? s/n ")

print("Encerrando por aqui, até a próxima!")