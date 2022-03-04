# Exercício 39: Série com Fatoriais no Denominador S = 1 + 1/1! + 1/2! + ... + 1/N!
# Enunciado:
# Elabore um programa em Python com uma função que recebe um valor inteiro e positivo N e retorna o valor de S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N! (Aproximação do número de Euler e).

import math

def calcular_serie_e(n):
    if n <= 0:
        return 1.0
    s = 1.0 + sum(1.0 / math.factorial(i) for i in range(1, n + 1))
    return s

n = int(input("Digite N para aproximação da série de Euler: "))
print(f"S = {calcular_serie_e(n):.8f}")
