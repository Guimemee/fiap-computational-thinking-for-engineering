# Exercício 27: Conceito Acadêmico por Nota Final
# Enunciado:
# Elabore um programa em Python com uma função que recebe a média final de um aluno e retorna o seu conceito, conforme a tabela abaixo:
- de 0,0 a 4,9: D
- de 5,0 a 6,9: C
- de 7,0 a 8,9: B
- de 9,0 a 10,0: A

def obter_conceito(media):
    if 0.0 <= media <= 4.9:
        return 'D'
    elif 5.0 <= media <= 6.9:
        return 'C'
    elif 7.0 <= media <= 8.9:
        return 'B'
    elif 9.0 <= media <= 10.0:
        return 'A'
    else:
        return 'Média inválida (fora do intervalo [0.0, 10.0])'

media = float(input("Digite a média final do aluno: "))
print(f"Conceito atribuído: {obter_conceito(media)}")
