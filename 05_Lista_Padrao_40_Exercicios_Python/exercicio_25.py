# Exercício 25: Função Booleana Positivo ou Negativo
# Enunciado:
# Elabore um programa em Python com uma função que recebe um valor inteiro e verifica se o valor é positivo ou negativo. A função deve retornar um valor booleano.

def eh_positivo(num):
    return num >= 0

val = int(input("Digite um valor inteiro: "))
print(f"É positivo (True) ou negativo (False)? {eh_positivo(val)}")
