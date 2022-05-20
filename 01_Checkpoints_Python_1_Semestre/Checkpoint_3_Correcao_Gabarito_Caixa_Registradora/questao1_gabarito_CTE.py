print("Gabarito da avaliação:\n01 - A\n02 - B\n03 - C\n04 - D\n05 - E\n06 - E\n07 - D\n08 - C\n09 - B\n10 - A")

questao = 1
ponto = 0

while questao <= 10:
    resposta = input(f"Resposta da questão {questao}: ")
    if questao == 1 and resposta == "A":
        ponto += 1
    elif questao == 2 and resposta == "B":
        ponto += 1
    elif questao == 3 and resposta == "C":
        ponto += 1
    elif questao == 4 and resposta == "D":
        ponto += 1
    elif questao == 5 and resposta == "E":
        ponto += 1
    elif questao == 6 and resposta == "E":
        ponto += 1
    elif questao == 7 and resposta == "D":
        ponto += 1
    elif questao == 8 and resposta == "C":
        ponto += 1
    elif questao == 9 and resposta == "B":
        ponto += 1
    elif questao == 10 and resposta == "A":
        ponto += 1
    questao += 1

print(f"A nota total é igual a {ponto} ponto (s).")