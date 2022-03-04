# Exercício 21: Conversão de Tempo (Horas, Minutos e Segundos) para Segundos
# Enunciado:
# Elabore um programa em Python com uma função que recebe o tempo de duração de um vídeo expresso em horas, minutos e segundos e retorna esse tempo em segundos.

def converter_para_segundos(horas, minutos, segundos):
    return (horas * 3600) + (minutos * 60) + segundos

h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))
print(f"Tempo total em segundos: {converter_para_segundos(h, m, s)} segundos")
