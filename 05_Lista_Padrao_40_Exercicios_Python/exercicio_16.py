# Exercício 16: Inversão de Número Inteiro
# Enunciado:
# Elabore um programa em Python com uma função que receba um número e imprima ele na ordem inversa. Ou seja, se recebeu o inteiro 123, deve imprimir o inteiro 321.

def inverter_numero(n):
    s = str(abs(n))
    inv = s[::-1]
    resultado = int(inv)
    return -resultado if n < 0 else resultado

num = int(input("Digite um número inteiro: "))
print(f"Número invertido: {inverter_numero(num)}")
