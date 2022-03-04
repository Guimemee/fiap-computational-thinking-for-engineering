# Exercício 24: Classificação de Nadador por Faixa Etária
# Enunciado:
# Elabore um programa em Python com uma função que recebe a idade de um nadador e retorna a categoria desse nadador de acordo com a tabela abaixo:
- 5 a 7 anos: Infantil A
- 8 a 10 anos: Infantil B
- 11 a 13 anos: Juvenil A
- 14 a 17 anos: Juvenil B
- Maiores de 18 anos (inclusive): Adulto

def categoria_nadador(idade):
    if 5 <= idade <= 7:
        return "Infantil A"
    elif 8 <= idade <= 10:
        return "Infantil B"
    elif 11 <= idade <= 13:
        return "Juvenil A"
    elif 14 <= idade <= 17:
        return "Juvenil B"
    elif idade >= 18:
        return "Adulto"
    else:
        return "Idade abaixo da faixa permitida para competição (menor que 5 anos)"

idade = int(input("Digite a idade do nadador: "))
print(f"Categoria: {categoria_nadador(idade)}")
