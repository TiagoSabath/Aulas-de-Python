
tamanho = int(input("Digite o tamanho da sequencia: "))

produto = 1
i = 0

while i < tamanho:
    valor = int(input("Digite um valor: "))
    produto = produto * valor
    i = i + 1

print("A soma total ", produto)