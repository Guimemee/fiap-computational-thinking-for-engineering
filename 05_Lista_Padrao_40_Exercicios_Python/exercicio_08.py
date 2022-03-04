# Exercício 08: Função Menor entre 3 Números
# Enunciado:
# Crie um programa com uma função em linguagem python que receba 3 números e retorne o menor valor.

def menor_de_tres(a, b, c):
    """Retorna o menor entre três números."""
    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    return menor

a = float(input("Digite o 1º número: "))
b = float(input("Digite o 2º número: "))
c = float(input("Digite o 3º número: "))
print(f"O menor valor entre os três é: {menor_de_tres(a, b, c)}")
