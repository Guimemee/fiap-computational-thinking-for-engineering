# Exercício 26: Função Booleana Par ou Ímpar
# Enunciado:
# Elabore um programa em Python com uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar. A função deve retornar um valor booleano.

def eh_par(num):
    return num % 2 == 0

val = int(input("Digite um valor inteiro: "))
print(f"É par? {eh_par(val)}")
