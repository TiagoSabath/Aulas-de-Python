numero = input("Digite um número inteiro: ")

adjacente = False

for i in range(len(numero) - 1):
    if numero[i] == numero[i + 1]:
        adjacente = True
        break

if adjacente:
    print("sim")
else:
    print("não")