# Exercício 13: Números Primos até 1000
# Enunciado:
# Elabore um programa em Python com uma função que acha todos os números primos até 1000. Número primo é aquele que é divisível somente por 1 e por ele mesmo.

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def listar_primos_ate_1000():
    primos = [n for n in range(2, 1001) if eh_primo(n)]
    print(f"Total de números primos até 1000: {len(primos)}")
    print("Primos encontrados:")
    print(primos)

listar_primos_ate_1000()
