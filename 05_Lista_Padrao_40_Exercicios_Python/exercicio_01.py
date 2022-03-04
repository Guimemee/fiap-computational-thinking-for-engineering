# Exercício 01: Função para Verificar se um Número é Positivo
# Enunciado:
# Crie um programa com uma função que receba um valor e informe se ele é positivo ou não.

def eh_positivo(valor):
    """Verifica se um número é positivo."""
    return valor > 0

# Teste interativo
num = float(input("Digite um número: "))
if eh_positivo(num):
    print(f"O número {num} é positivo.")
else:
    print(f"O número {num} não é positivo.")
