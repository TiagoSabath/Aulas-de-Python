nota1 = float (input("Digite sua primeira nota "))
nota2 = float (input("Digite sua segunda nota "))

nota = (nota1 + nota2) / 2

if nota >= 9.0:
    print("Aprovado    A  " , nota)
elif nota >= 7.5:
    print("Aprovado    B  " , nota)
elif nota >= 6.0:
    print("Aprovado    C  " , nota)
elif nota >= 4.0:
    print("Reprovado    D  " , nota)
else:
    print("Reprovado    E  " , nota)