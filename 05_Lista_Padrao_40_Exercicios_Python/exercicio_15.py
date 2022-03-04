# Exercício 15: Números Perfeitos até 1000
# Enunciado:
# Elabore um programa em Python com uma função que ache todos os números perfeitos até 1000. Número perfeito é aquele que é a soma de seus fatores. Por exemplo, 6 é divisível por 1, 2 e 3 ao passo que 6 = 1 + 2 + 3.

def eh_perfeito(n):
    if n < 2:
        return False
    fatores = [i for i in range(1, n) if n % i == 0]
    return sum(fatores) == n

def listar_perfeitos():
    perfeitos = [n for n in range(1, 1001) if eh_perfeito(n)]
    print(f"Números perfeitos até 1000: {perfeitos}")

listar_perfeitos()
