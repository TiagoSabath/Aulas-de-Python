n = int(input("Digite um número inteiro positivo: "))

contador = 0

numero_impar = 1

print("Os", n, "primeiros números ímpares naturais são:")
while contador < n:
    print(numero_impar)
    numero_impar += 2
    contador += 1
