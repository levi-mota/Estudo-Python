nome_da_empresa = input("Qual o nome da empresa? ")
valor_servico = float(input("Qual o valor do serviço? "))
aliquota_iss = float(input("Qual a aliquota? "))
valor_imposto = valor_servico * aliquota_iss
print(f"o valor calculado para a empresa {nome_da_empresa} e {valor_imposto:.4f}")