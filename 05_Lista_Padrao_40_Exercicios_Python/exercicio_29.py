# Exercício 29: Duração de um Jogo em Minutos (Cruzamento de Meia-Noite)
# Enunciado:
# Elabore um programa em Python com uma função que recebe a hora de inicio e a hora de término de um jogo, ambas subdivididas em 2 valores distintos: horas e minutos. O procedimento deve retornar a duração do jogo em minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que o jogo pode começar em um dia e terminar no outro.

def duracao_jogo_minutos(h_ini, m_ini, h_fim, m_fim):
    minutos_inicio = (h_ini * 60) + m_ini
    minutos_fim = (h_fim * 60) + m_fim
    
    if minutos_fim >= minutos_inicio:
        duracao = minutos_fim - minutos_inicio
    else:
        duracao = (24 * 60 - minutos_inicio) + minutos_fim
    return duracao

h1 = int(input("Hora de início: "))
m1 = int(input("Minuto de início: "))
h2 = int(input("Hora de término: "))
m2 = int(input("Minuto de término: "))

duracao = duracao_jogo_minutos(h1, m1, h2, m2)
print(f"Duração total do jogo: {duracao} minutos ({duracao // 60}h {duracao % 60}min)")
