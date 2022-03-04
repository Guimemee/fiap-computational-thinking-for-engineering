# Exercício 18: Cálculo de Médias (Aritmética, Ponderada e Harmônica)
# Enunciado:
# Elabore um programa em Python com uma função que recebe as 3 notas de um aluno e uma letra. Se a letra for A o procedimento calcula a média aritmética das notas do aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2) e se for H, a sua média harmônica. A média calculada deve ser retornada.

def calcular_media(n1, n2, n3, tipo):
    tipo = tipo.upper()
    if tipo == 'A':
        return (n1 + n2 + n3) / 3.0
    elif tipo == 'P':
        return ((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10.0
    elif tipo == 'H':
        return 3.0 / ((1.0 / n1) + (1.0 / n2) + (1.0 / n3))
    else:
        raise ValueError("Tipo de média inválido. Use A, P ou H.")

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
tipo = input("Tipo de Média (A - Aritmética, P - Ponderada, H - Harmônica): ")
print(f"Média calculada: {calcular_media(n1, n2, n3, tipo):.2f}")
