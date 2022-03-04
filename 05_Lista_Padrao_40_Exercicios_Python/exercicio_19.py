# Exercício 19: Função Booleana para Teste de Primalidade
# Enunciado:
# Elabore um programa em Python com uma função que recebe um valor inteiro e positivo e retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso contrário.

def eh_primo(valor):
    if valor <= 1:
        return False
    for i in range(2, int(valor**0.5) + 1):
        if valor % i == 0:
            return False
    return True

num = int(input("Digite um número inteiro positivo: "))
print(f"É primo? {eh_primo(num)}")
