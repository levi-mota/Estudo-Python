print("Bem-vindo(a) ao sistema lista de compras")
lista = []
lista.append({"nome":input("Qual o nome do produto: "), "qtd":int(input("Qual a quantidade: "))})
print(f"Produto {lista[-1]['nome']} (Quantidade: {lista[-1]['qtd']}) adicionado com sucesso!\n")
novo_produto = input("Deseja adicionar outro produto a lista de compras? s/n ")

while novo_produto == "s":
    lista.append({"nome":input("Qual o nome do produto: "), "qtd":int(input("Qual a quantidade: "))})
    print(f"Produto {lista[-1]['nome']} (Quantidade: {lista[-1]['qtd']}) adicionado com sucesso!\n")
    novo_produto = input("Deseja adicionar outro produto a lista de compras? s/n ")

    
lista.sort(key=lambda x: x['nome'])
total_itens = len(lista)

print(f"Segue sua lista com o total de itens {total_itens}")
for itens in lista:
    print(f"- {itens['nome']} | {itens['qtd']}")