# Exercício 09: Simulação de Sorteio de Dado
# Enunciado:
# Crie um programa com uma função em linguagem python chamada Dado() que retorna, através de sorteio, um número de 1 até 6.

import random

def Dado():
    """Retorna um número aleatório entre 1 e 6."""
    return random.randint(1, 6)

print(f"Resultado do lançamento do dado: {Dado()}")
