# Exercício 38: Série Harmônica S = 1 + 1/2 + 1/3 + ... + 1/N
# Enunciado:
# Elabore um programa em Python com uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N.

def calcular_serie_harmonica(n):
    if n <= 0:
        return 0.0
    s = sum(1.0 / i for i in range(1, n + 1))
    return s

n = int(input("Digite N para o cálculo de S: "))
print(f"S = {calcular_serie_harmonica(n):.6f}")
