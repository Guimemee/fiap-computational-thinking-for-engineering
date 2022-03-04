# Exercício 30: Verificação e Classificação de Triângulos
# Enunciado:
# Elabore um programa em Python com uma função que recebes 3 valores reais X, Y e Z e que verifique se esses valores podem ser os comprimentos dos lados de um triângulo e, neste caso, retornar qual o tipo de triângulo formado. Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade seja satisfeita: o comprimento de cada lado de um triângulo é menor do que a soma do comprimento dos outros dois lados. O procedimento deve identificar o tipo de triângulo formado: Equilátero (3 lados iguais), Isósceles (2 lados iguais), Escaleno (3 lados diferentes).

def classificar_triangulo(x, y, z):
    # Validação da Desigualdade Triangular
    if (x < y + z) and (y < x + z) and (z < x + y):
        if x == y == z:
            return "Triângulo Equilátero"
        elif x == y or x == z or y == z:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "Os lados informados não formam um triângulo."

x = float(input("Lado X: "))
y = float(input("Lado Y: "))
z = float(input("Lado Z: "))
print(f"Classificação: {classificar_triangulo(x, y, z)}")
