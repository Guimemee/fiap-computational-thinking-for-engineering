# Exercício 34: Maior e Menor entre 50 Valores Inteiros
# Enunciado:
# Elabore um programa em Python com uma função que lê 50 valores inteiros e retorna o maior e o menor deles.

def maior_menor_50(lista_valores=None):
    if lista_valores is None:
        lista_valores = []
        print("Digite 50 valores inteiros:")
        for i in range(50):
            val = int(input(f"Valor {i+1}/50: "))
            lista_valores.append(val)
    return max(lista_valores), min(lista_valores)

# Exemplo com conjunto demonstrativo
amostra = list(range(1, 51))
maior, menor = maior_menor_50(amostra)
print(f"Maior valor: {maior} | Menor valor: {menor}")
