valor1 = int(input("Digite o valor para ser multiplicado: "))

if 1 <= valor1 <= 10:
    print(f"Tabuada de {valor1}:")
    for i in range(1, 11):
        resultado = valor1 * i
        print(f"{valor1} X {i} = {resultado}")