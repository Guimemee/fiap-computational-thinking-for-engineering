
import os

carros = []
taxaPadrao = 0

with open("ListaDeCarros.txt", "r", encoding='utf-8') as arquivo:
    carros = arquivo.read().split("\n")

print("Caminhão\n"
      "Furgão\n"
      "Picape\n"
      "SUV\n"
      "HATCHBACK\n"
      "SEDAN\n")

escolha = input("Escolha uma categoria carro elétrico disponível:").upper()

while escolha != "CAMINHÃO" and escolha != "FURGÃO" and escolha != "PICAPE" and escolha != "SUV" and escolha != "HATCHBACK" and escolha != "SEDAN":
    escolha = input("Digite uma das categorias (Caminhão, Furgão, Picape, SUV, Hatchback, Sedan):").upper()

if escolha == "CAMINHÃO":
    taxaPadrao = 15.90
    for caminhao in carros:
        if caminhao.startswith("Caminhão"):
            print(caminhao)
    carro = input("Selecione um Caminhão:")
elif escolha == "FURGÃO":
    taxaPadrao = 12.90
    for furgao in carros:
        if furgao.startswith("Furgão"):
            print(furgao)
    carro = input("Selecione um Furgão:")
elif escolha == "PICAPE":
    taxaPadrao = 8.90
    for picape in carros:
        if picape.startswith("Picape"):
            print(picape)
    carro = input("Selecione uma Picape:")
elif escolha == "SUV":
    taxaPadrao = 6.90
    for SUV in carros:
        if SUV.startswith("SUV"):
            print(SUV)
    carro = input("Selecione uma SUV:")
elif escolha == "HATCHBACK":
    taxaPadrao = 4.90
    for hatchback in carros:
        if hatchback.startswith("Hatchback"):
            print(hatchback)
    carro = input("Selecione um Hatchback:")
elif escolha == "SEDAN":
    taxaPadrao = 3.90
    for sedan in carros:
        if sedan.startswith("Sedan"):
            print(sedan)
    carro = input("Selecione um Sedan:")

os.system('cls')

print(f"\nAté 6 horas: R$ {taxaPadrao} mais R$ 0,70 (por minuto) \n"
      f"A partir de 6 horas: R$ {taxaPadrao} mais R$ 0,40 (por minuto)\n"
      f"A partir de 12 horas: R$ {taxaPadrao} mais R$ 0,30 (por minuto)\n"
      f"A partir de 24 horas: R$ {taxaPadrao} mais R$ 0,20 (por minuto)\n"
      f"A partir de 48 horas: R$ {taxaPadrao} mais R$ 0,18 (por minuto)\n")

horas = float(input("Quantas horas gostaria de utilizar o carro? "))


if horas > 0 and horas < 6:
    preco = (horas * 60) * 0.7 + taxaPadrao
elif horas >= 6 and horas < 12:
    preco = (horas * 60) * 0.4 + taxaPadrao
elif horas >= 12 and horas < 24:
    preco = (horas * 60) * 0.3 + taxaPadrao
elif horas >= 24 and horas < 48:
    preco = (horas * 60) * 0.2 + taxaPadrao
elif horas >= 48:
    preco = (horas * 60) * 0.18 + taxaPadrao

print((f"O aluguel do carro elétrico {carro}, no período de {round(horas)}h, ficará no valor de R$%.2f."%preco))
print("Verifique o arquivo ResumoAluguel.txt")

with open("ResumoAluguel.txt", "a", encoding='utf-8') as arquivo:
    arquivo.write(f"O aluguel do carro elétrico {carro}, no período de {round(horas)}h, ficará no valor de R$%.2f.\n"%preco)