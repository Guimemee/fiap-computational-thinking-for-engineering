# Exercício 03: Cálculo do Delta de uma Equação do 2º Grau
# Enunciado:
# Crie um programa com uma função que receba três valores, 'a', 'b' e 'c', que são os coeficientes de uma equação do segundo grau e retorne o valor do delta, que é dado por 'b² - 4ac'

def calcular_delta(a, b, c):
    """Calcula o discriminante delta de uma equação do 2º grau."""
    return (b ** 2) - (4 * a * c)

# Teste interativo
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = calcular_delta(a, b, c)
print(f"O discriminante Delta é: {delta}")
