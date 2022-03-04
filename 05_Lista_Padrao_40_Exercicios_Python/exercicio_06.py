# Exercício 06: Função Menor entre 2 Números
# Enunciado:
# Crie um programa com uma função em linguagem python que receba 2 números e retorne o menor valor.

def menor_de_dois(n1, n2):
    """Retorna o menor entre dois números."""
    if n1 < n2:
        return n1
    return n2

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print(f"O menor valor é: {menor_de_dois(n1, n2)}")
