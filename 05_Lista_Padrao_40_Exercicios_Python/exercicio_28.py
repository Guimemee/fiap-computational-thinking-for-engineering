# Exercício 28: Cálculo do Peso Ideal por Altura e Sexo
# Enunciado:
# Elabore um programa em Python com uma função que recebe a altura (alt) e o sexo de uma pessoa e retorna o seu peso ideal. Para homens, calcular o peso ideal usando a fórmula peso ideal = 72.7 x alt - 58 e, para mulheres, peso ideal = 62.1 x alt - 44.7.

def peso_ideal(altura, sexo):
    sexo = sexo.strip().upper()
    if sexo == 'M':
        return (72.7 * altura) - 58.0
    elif sexo == 'F':
        return (62.1 * altura) - 44.7
    else:
        raise ValueError("Sexo inválido. Utilize 'M' para masculino ou 'F' para feminino.")

alt = float(input("Digite a altura em metros (ex: 1.75): "))
sexo = input("Digite o sexo (M/F): ")
print(f"Peso ideal calculado: {peso_ideal(alt, sexo):.2f} kg")
