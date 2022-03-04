# Exercício 37: Somatório de 1 até N
# Enunciado:
# Elabore um programa em Python com uma função que recebe um valor inteiro e positivo e retorna o somatório desse valor (1 + 2 + ... + N).

def somatorio(n):
    if n <= 0:
        return 0
    return (n * (n + 1)) // 2

val = int(input("Digite um valor inteiro positivo N: "))
print(f"O somatório de 1 até {val} é: {somatorio(val)}")
