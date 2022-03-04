# Exercício 17: Volume de uma Esfera
# Enunciado:
# Elabore um programa em Python com uma função que recebe o raio de uma esfera e calcula o seu volume (v = 4/3 * Pi * R³).

import math

def volume_esfera(raio):
    return (4.0 / 3.0) * math.pi * (raio ** 3)

r = float(input("Digite o raio da esfera: "))
print(f"O volume da esfera de raio {r} é: {volume_esfera(r):.4f}")
