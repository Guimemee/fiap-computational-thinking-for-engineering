# Exercício 22: Conversão de Idade (Anos, Meses e Dias) para Dias
# Enunciado:
# Elabore um programa em Python com uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.

def idade_em_dias(anos, meses, dias):
    # Considerando 1 ano = 365 dias e 1 mês = 30 dias
    return (anos * 365) + (meses * 30) + dias

a = int(input("Anos: "))
m = int(input("Meses: "))
d = int(input("Dias: "))
print(f"Idade total expressa em dias: {idade_em_dias(a, m, d)} dias")
