# Exercício 07: Função Maior entre 3 Números
# Enunciado:
# Crie um programa com uma função em linguagem python que receba 3 números e retorne o maior valor.

def maior_de_tres(a, b, c):
    """Retorna o maior entre três números."""
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior

a = float(input("Digite o 1º número: "))
b = float(input("Digite o 2º número: "))
c = float(input("Digite o 3º número: "))
print(f"O maior valor entre os três é: {maior_de_tres(a, b, c)}")
