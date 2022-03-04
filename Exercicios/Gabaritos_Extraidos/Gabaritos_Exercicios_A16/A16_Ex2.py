def avalia_letra(ltr):
    if ltr>='a' and ltr<='z':
        return 'm'
    else:
        return 'M'

while 1:
    letra=input("informe uma letra:")

    res=avalia_letra(letra)

    if(res=='m'):
        print("Letra Minúscula!")
    else:
        print("Letra Maiúscula!")
