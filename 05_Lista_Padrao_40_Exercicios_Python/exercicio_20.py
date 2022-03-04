# Exercício 20: Resolução da Fórmula de Bhaskara
# Enunciado:
# Elabore um programa em Python com uma função que recebe os valores necessários para o cálculo da fórmula de báskara e imprime as suas raízes, caso seja possível calcular.

import math

def bhaskara(a, b, c):
    if a == 0:
        print("Coeficiente 'a' não pode ser 0.")
        return
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print("Não existem raízes reais para a equação (Delta < 0).")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Raiz x1 = {x1:.4f}")
        print(f"Raiz x2 = {x2:.4f}")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
bhaskara(a, b, c)
