# Exercício 04: Cálculo das Raízes da Equação do 2º Grau (Reais e Complexas)
# Enunciado:
# Usando as 3 funções acima, crie um programa que calcula as raízes de uma equação do 2o grau: ax² + bx + c = 0. Para ela existir, o coeficiente 'a' deve ser diferente de zero. Caso o delta seja maior ou igual a zero, as raízes serão reais. Caso o delta seja negativo, as raízes serão complexas e da forma: x + iy

import math

def eh_nulo(valor):
    return valor == 0

def eh_positivo(valor):
    return valor >= 0

def calcular_delta(a, b, c):
    return (b ** 2) - (4 * a * c)

def resolver_equacao_2grau(a, b, c):
    if eh_nulo(a):
        print("Erro: O coeficiente 'a' não pode ser zero para uma equação do 2º grau.")
        return
    
    delta = calcular_delta(a, b, c)
    print(f"Delta = {delta}")
    
    if eh_positivo(delta):
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Raízes reais: x1 = {x1:.4f}, x2 = {x2:.4f}")
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-delta) / (2 * a)
        print(f"Raízes complexas: x1 = {real:.4f} + {imag:.4f}i, x2 = {real:.4f} - {imag:.4f}i")

# Teste interativo
a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))
resolver_equacao_2grau(a, b, c)
