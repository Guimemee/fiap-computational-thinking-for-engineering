# Exercício 02: Função para Verificar se um Número é Nulo
# Enunciado:
# Crie um programa com uma função que receba um valor e diga se é nulo ou não.

def eh_nulo(valor):
    """Verifica se um número é nulo (igual a zero)."""
    return valor == 0

# Teste interativo
num = float(input("Digite um número: "))
if eh_nulo(num):
    print(f"O número {num} é nulo (zero).")
else:
    print(f"O número {num} não é nulo.")
