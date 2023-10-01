decrescente = True
anterior = int(input("Digite o primeiro numero: "))

valor = 1

while valor != 0 and decrescente:
    valor = int(input("Digit o proximo numero: "))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente:
    print ("A sequncia está em ordem decrescente")
else :
    print ("A sequncia não está em ordem decrescente")