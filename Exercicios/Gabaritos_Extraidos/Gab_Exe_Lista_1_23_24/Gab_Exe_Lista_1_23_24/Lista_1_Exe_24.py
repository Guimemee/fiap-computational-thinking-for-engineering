def categoria(idade):
    if idade >= 5 and idade <= 7:
        return "Infantil A"
    elif idade >= 8 and idade <= 10:
        return "Infantil B"
    elif idade >= 11 and idade <= 13:
        return "Juvenil A"
    elif idade >= 14 and idade <= 17:
        return "Juvenil B"
    elif idade >= 18:
        return "Adulto"
    else:
        return "Inexistente"

while 1:
    x = int(input("Qual é a idade do nadador?"))
    #cat=categoria(x)
    #print("Categoria ",cat)
    print "Categoria ",categoria(x)
