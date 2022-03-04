# Exercício 35: Tabuada Personalizada de 1 até N
# Enunciado:
# Elabore um programa em Python com uma função que recebe um valor N e calcula e escreve a tabuada de 1 até N.

def tabuada_ate_n(n):
    print(f"=== TABUADA DE 1 ATÉ {n} ===")
    for i in range(1, n + 1):
        print(f"{i} x {n} = {i * n}")

n = int(input("Digite o valor de N: "))
tabuada_ate_n(n)
