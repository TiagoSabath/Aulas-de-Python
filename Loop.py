lista_valores = list(range(10 , 20))
iteracoes = 0
for valor in lista_valores:
    print(valor)
    iteracoes += 1
    if iteracoes >= 6:
        break
