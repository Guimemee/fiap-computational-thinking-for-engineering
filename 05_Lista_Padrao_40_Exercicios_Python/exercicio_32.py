# Exercício 32: Média Aritmética de Valores Positivos Indeterminados
# Enunciado:
# Elabore um programa em Python com uma função que leia um número não determinado de valores positivos e retorna a média aritmética dos mesmos.

def media_positivos():
    valores = []
    print("Digite valores positivos (digite um número negativo para finalizar):")
    while True:
        v = float(input("Valor: "))
        if v < 0:
            break
        valores.append(v)
    if valores:
        return sum(valores) / len(valores)
    return 0.0

m = media_positivos()
print(f"Média aritmética dos valores positivos: {m:.2f}")
