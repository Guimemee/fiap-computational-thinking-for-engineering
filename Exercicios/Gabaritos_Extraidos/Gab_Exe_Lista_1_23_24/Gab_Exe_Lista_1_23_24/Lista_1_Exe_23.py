def verificador(x):
    soma = 0
    for i in range(1,x,1):
        if x % i == 0:
            soma+=i #soma=soma+i
    if soma == x:
        return 1 #é perfeito
    else:
        return 0 #não é perfeito

while 1:
    num=int(input("Informe valor inteiro e positivo:"))

    ret = verificador(num)

    if ret == 1:
        print("É perfeito!")
    else:
        print("Não é perfeito!")
