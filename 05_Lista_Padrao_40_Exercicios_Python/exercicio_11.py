# Exercício 11: Conversor de Temperaturas Celsius e Fahrenheit
# Enunciado:
# Com função, crie um programa de conversão entre as temperaturas Celsius e Farenheit. Primeiro o usuário deve escolher se vai entrar com a temperatura em Célsius ou Farenheit, depois a conversão escolhida é realizada através de comandos IF. Se C é a temperatura em Célsius e F em Farenheit, as fórmulas de conversão são: C = 5*(F-32)/9 e F = (9*C/5) + 32.

def celsius_para_fahrenheit(c):
    return (9 * c / 5) + 32

def fahrenheit_para_celsius(f):
    return 5 * (f - 32) / 9

print("=== CONVERSOR DE TEMPERATURA ===")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")
op = input("Escolha a opção (1 ou 2): ")

if op == '1':
    c = float(input("Digite a temperatura em ºC: "))
    print(f"{c} ºC = {celsius_para_fahrenheit(c):.2f} ºF")
elif op == '2':
    f = float(input("Digite a temperatura em ºF: "))
    print(f"{f} ºF = {fahrenheit_para_celsius(f):.2f} ºC")
else:
    print("Opção inválida.")
