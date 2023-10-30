minha_lista = [100, 7, 22.2, "João", 92, 21.0, 45, 22, 32, "Maria"]

soma = 0
valores_descartados = []

for valor in minha_lista:
    if isinstance(valor, (int, float)) and valor < 90:
        soma += valor
    else:
        valores_descartados.append(valor)

print("Valores descartados:", valores_descartados)

print("Soma dos valores aceitos:", soma)