itens = {100: ("Cachorro Quente", 1.20), 101: ("Bauru Simples", 1.30), 102: ("Bauru com ovo", 1.50),
103: ("Hambúrguer", 1.20), 104: ("Cheeseburguer", 1.30), 105: ("Refrigerante", 1.00)}

print("Especificação   Código   Preço ")
print("")
for codigo, (nome, preco) in itens.items():
    print(f"{nome:<15}  {codigo:<5}  {preco:.2f}")

total_pedido = 0

while True:
    print("")
    codigo = int(input("Digite o código do item (ou -1 para encerrar o pedido): "))
    if codigo == -1:
        break

    if codigo in itens:
        quantidade = int(input("Digite a quantidade desejada: "))
        nome, preco_unitario = itens[codigo]
        valor_item = preco_unitario * quantidade
        total_pedido += valor_item
        print(f"Item: {nome}, Preço: R$ {preco_unitario:.2f}, Quantidade: {quantidade}, Valor: R$ {valor_item:.2f}")
    else:
        print("Código de item inválido. Por favor, insira um código válido.")

print(f"Total do pedido: R$ {total_pedido:.2f}")