# Exercício 40: Exponenciação Manual (X elevado a Z sem operador pronto)
# Enunciado:
# Elabore um programa em Python com uma função que recebe dois valores X e Z e calcula e retorna X elevado a Z sem utilizar funções ou operadores de potência prontos.

def potencia_manual(x, z):
    if z == 0:
        return 1.0
    resultado = 1.0
    expoente_positivo = abs(z)
    for _ in range(expoente_positivo):
        resultado *= x
    if z < 0:
        return 1.0 / resultado
    return resultado

x = float(input("Digite a base X: "))
z = int(input("Digite o expoente Z (inteiro): "))
print(f"{x}^{z} = {potencia_manual(x, z)}")
