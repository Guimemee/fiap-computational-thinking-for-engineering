# Exercício 12: Cálculo de Média com Descarte da Menor de 3 Notas
# Enunciado:
# Um professor, muito legal, fez 3 provas durante um semestre mas só vai levar em conta as duas notas mais altas para calcular a média. Faça um programa em python que peça o valor das 3 notas, execute uma função que mostre como seria a média com essas 3 provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.

def analisar_notas(n1, n2, n3):
    notas = [n1, n2, n3]
    notas_ordenadas = sorted(notas)
    
    media_todas = sum(notas) / 3.0
    media_duas_maiores = (notas_ordenadas[1] + notas_ordenadas[2]) / 2.0
    maior_nota = max(notas)
    menor_nota = min(notas)
    
    print(f"Média com as 3 provas: {media_todas:.2f}")
    print(f"Média com as 2 maiores notas ({notas_ordenadas[1]}, {notas_ordenadas[2]}): {media_duas_maiores:.2f}")
    print(f"Nota mais alta: {maior_nota}")
    print(f"Nota mais baixa (descartada): {menor_nota}")

n1 = float(input("Digite a Nota 1: "))
n2 = float(input("Digite a Nota 2: "))
n3 = float(input("Digite a Nota 3: "))
analisar_notas(n1, n2, n3)
