# Exercício 23: Função Booleana para Número Perfeito
# Enunciado:
# Elabore um programa em Python com uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito quando ele é igual a soma dos seus divisores excetuando ele próprio. (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar um valor booleano.

def verificar_perfeito(num):
    if num <= 0:
        return False
    soma_divisores = sum([i for i in range(1, num) if num % i == 0])
    return soma_divisores == num

val = int(input("Digite um número: "))
print(f"O número {val} é perfeito? {verificar_perfeito(val)}")
