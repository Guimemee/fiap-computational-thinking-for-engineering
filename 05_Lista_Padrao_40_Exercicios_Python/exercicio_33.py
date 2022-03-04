# Exercício 33: Cálculo de Fatorial
# Enunciado:
# Elabore um programa em Python com uma função que receba um valor inteiro e positivo e calcula o seu fatorial.

def fatorial(n):
    if n < 0:
        raise ValueError("O fatorial não é definido para números negativos.")
    fat = 1
    for i in range(2, n + 1):
        fat *= i
    return fat

num = int(input("Digite um número inteiro positivo: "))
print(f"{num}! = {fatorial(num)}")
