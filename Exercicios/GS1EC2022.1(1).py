while True:

    print()
    print("***CÁLCULO DO CONSUMO MÉDIO DE UM CARRO ELÉTRICO***")
    print()

    carro_ele = input("Qual o carro? ")
    bateria = int(input("Qual a bateria do carro em kWh? "))
    autonomia = int(input("Qual a autonomia da bateria em km? "))
    valor_ele = float(input("Qual o valor de cada kWh para abastecer? R$ "))

    consumo_medio_ele = (bateria * 100) / autonomia

    gasto_ele = consumo_medio_ele * valor_ele

    print()
    print(f"O consumo médio do carro {carro_ele} é de {consumo_medio_ele:.2f} kWh a cada 100 km rodados.")
    print(f"O gasto do carro elétrico {carro_ele} é de R$ {gasto_ele:.2f} para rodar 100 km.")

    print()
    print("***CÁLCULO DO CONSUMO MÉDIO DE UM CARRO A COMBUSTÃO***")
    print()

    carro_comb = input("Qual o carro? ")
    litros_100km = int(input(f"Quantos litros são necessários para o carro rodar 100 km? "))
    valor_comb = float(input("Qual o valor do litro do combustível? R$ "))

    gasto_comb = litros_100km * valor_comb

    print()
    print(f"O gasto com o carro a combustão {carro_comb} é de R$ {gasto_comb:.2f} para rodar 100 km.")

    print()
    print("***COMPARAÇÃO***")
    print()

    comp = gasto_comb / gasto_ele

    if comp > 1:
        print(f'''O gasto com o carro elétrico {carro_ele} é {comp:.0f} vezes menor em comparação com o carro a combustão {carro_comb}.''')
    else:
        print(f''' gasto com o carro a combustão {carro_comb} é {(1/comp):.0f} vezes menor em comparação com o carro a elétrico {carro_ele}.''')

    print()
    print()
    continuar = input("Gostaria de realizar outro cálculo (SIM/NÃO)? ").upper()
    if continuar == "NÃO":
        break
