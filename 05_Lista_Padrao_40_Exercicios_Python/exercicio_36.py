# Exercício 36: Contagem de Divisores de um Número Inteiro
# Enunciado:
# Elabore um programa em Python com uma função que recebe um valor inteiro e positivo e retorna o número de divisores desse valor.

def contar_divisores(n):
    if n <= 0:
        return 0
    divisores = [i for i in range(1, n + 1) if n % i == 0]
    return len(divisores)

val = int(input("Digite um valor inteiro positivo: "))
print(f"O número {val} possui {contar_divisores(val)} divisores.")
