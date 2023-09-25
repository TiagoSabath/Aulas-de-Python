#### Exercício 1 - Par ou ímpar? #####

num = int(input("Digite um número: "))

if num % 2 == 0:
    print("Esse número e Par")
else :
    print("Esse número e Impar")


#### Exercicios 2 - FizzBuzz parcial, parte 1 #####

num = int(input("Digite um número: "))

if num % 3 == 0:
    print("Fizz")
else:
    print(num)

#### Exercícios 3 - FizzBuzz parcial, parte 2 #####

num = int(input("Digite um número: "))

if num % 5 == 0:
    print("Buzz")
else:
    print(num)

#### Exercícios 4 - FizzBuzz parcial, parte 3 #####

num = int(input("Digite um número: "))

if num % 3 == 0 & num % 5 == 0:
    print("FizzBuzz")
else:
    print(num)

#### Exercício 5 - Verificando ordenação #####

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 < num2 < num3:
    print("crescente")
else:
    print("não está em ordem crescente")