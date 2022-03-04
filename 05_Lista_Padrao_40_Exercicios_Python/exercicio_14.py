# Exercício 14: Máximo Divisor Comum (MDC)
# Enunciado:
# Elabore um programa em Python com uma função que recebe dois inteiros e retorna o MDC, máximo divisor comum.

def mdc(a, b):
    """Calcula o MDC pelo Algoritmo de Euclides."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

num1 = int(input("Digite o 1º número inteiro: "))
num2 = int(input("Digite o 2º número inteiro: "))
print(f"O MDC({num1}, {num2}) é: {mdc(num1, num2)}")
