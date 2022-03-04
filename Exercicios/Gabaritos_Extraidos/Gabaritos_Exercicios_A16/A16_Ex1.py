def paridade(x):
    if x % 2 == 0:
        #é par
        return 1
    else:
        #é impar
        return 0

while 1:
    z=input("Informe valor inteiro positivo:")
    z=int(z)

    resposta = paridade(z)

    if resposta == 0:
        print("É ímpar!")
    else:
        print("É par!")
