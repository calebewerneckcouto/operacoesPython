'''Escreva um programa que receba um número inteiro do usuário e imprima True
caso o número seja par e False, caso o número seja ímpar'''


n = int(input("Informe um valor:"))

if n %2 == 0:
    print(f"O numero {n} é PAR")
else:
    print(f"O numero {n} é IMPAR")