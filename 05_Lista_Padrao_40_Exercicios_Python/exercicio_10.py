# Exercício 10: Simulação de 1 Milhão de Lançamentos de Dado (Monte Carlo)
# Enunciado:
# Use a função da questão anterior e lance o dado 1 milhão de vezes. Conte quantas vezes cada número saiu. A probabilidade deu certo? Ou seja, a porcentagem dos números foi parecida?

import random

def Dado():
    return random.randint(1, 6)

total_lancamentos = 1_000_000
contadores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

print(f"Simulando {total_lancamentos:,} lançamentos de dado...")
for _ in range(total_lancamentos):
    face = Dado()
    contadores[face] += 1

print("\n=== RESULTADO DA CONTAGEM E PROBABILIDADE ===")
for face, cont in contadores.items():
    pct = (cont / total_lancamentos) * 100
    print(f"Face {face}: {cont:,} vezes ({pct:.2f}%) - Esperado teórico: ~16.67%")
