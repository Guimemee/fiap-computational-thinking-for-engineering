from random import choice

print('\nBem-vindo(a) ao jogo do PEDRA, PAPEL OU TESOURA (Jokenpô)!')

while True:

    jogador = input('\nEscolha PEDRA, PAPEL ou TESOURA? ').upper().strip()
    while True:
        if jogador == "PEDRA" or jogador == "PAPEL" or jogador == "TESOURA":
            break
        else:
            while True:
                jogador = input('Você digitou errado! Escolha PEDRA, PAPEL ou TESOURA? ').upper().strip()
                if jogador == "PEDRA" or jogador == "PAPEL" or jogador == "TESOURA":
                    break
        if jogador == "PEDRA" or jogador == "PAPEL" or jogador == "TESOURA":
            break

    opcao = ['PEDRA', 'PAPEL', 'TESOURA']
    computador = choice(opcao)

    if jogador == 'PEDRA' and computador == 'PEDRA':
        print(f'Empate! \nO computador escolheu {computador}.')
    elif jogador == 'PEDRA' and computador == 'PAPEL':
        print(f'Você perdeu! \nO computador escolheu {computador}.')
    elif jogador == 'PEDRA' and computador == 'TESOURA':
        print(f'Você venceu! \nO computador escolheu {computador}.')
    elif jogador == 'PAPEL' and computador == 'PEDRA':
        print(f'Você venceu! \nO computador escolheu {computador}.')
    elif jogador == 'PAPEL' and computador == 'PAPEL':
        print(f'Empate! \nO computador escolheu {computador}.')
    elif jogador == 'PAPEL' and computador == 'TESOURA':
        print(f'Você perdeu! \nO computador escolheu {computador}.')
    elif jogador == 'TESOURA' and computador == 'PEDRA':
        print(f'Você perdeu! \nO computador escolheu {computador}.')
    elif jogador == 'TESOURA' and computador == 'PAPEL':
        print(f'Você venceu! \nO computador escolheu {computador}.')
    else:
        print(f'Empate! \nO computador escolheu {computador}.')

    novo_jogo = input("\nDeseja jogar novamente (S - sim ou N - não)? ").upper().strip()
    if novo_jogo == "N":
        break
    elif novo_jogo != "S":
        while True:
            novo_jogo = input("Você digitou errado! Deseja jogar novamente (S - sim ou N - não)? ").upper().strip()
            if novo_jogo == "N" or novo_jogo == "S":
                break
    if novo_jogo == "N":
        break
