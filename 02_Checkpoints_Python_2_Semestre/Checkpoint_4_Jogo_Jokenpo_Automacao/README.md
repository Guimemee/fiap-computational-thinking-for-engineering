# Checkpoint 4: Jogo Jokenpô em Python

> Desenvolver um programa em Python que implemente o clássico jogo Jokenpô (Pedra, Papel e Tesoura) contra o computador.
> 
> **Requisitos do Programa:**
> 1. Apresentar um menu interativo com as opções: (1) Pedra, (2) Papel, (3) Tesoura, (0) Sair.
> 2. O computador deve realizar uma jogada pseudoaleatória entre as 3 opções.
> 3. Avaliar as regras do jogo:
>    - Pedra quebra Tesoura.
>    - Tesoura corta Papel.
>    - Papel embrulha Pedra.
>    - Jogadas iguais resultam em empate.
> 4. Manter o placar acumulado de vitórias do jogador, vitórias da máquina e empates até que o usuário decida encerrar.

### Link do Código:
- 🔗 [`jokenpo(4).py`](./jokenpo(4).py)

### Resolução:
```python
# Checkpoint 4 - Jogo Jokenpô Automatizado contra o Computador com Placar
import random

opcoes = ["Pedra", "Papel", "Tesoura"]
vitorias_jogador = 0
vitorias_computador = 0
empates = 0

print("=== JOGO JOKENPÔ (PEDRA, PAPEL, TESOURA) ===")

while True:
    print("\nEscolha sua jogada:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("0 - Sair do Jogo")
    
    escolha = int(input("Sua escolha: "))
    if escolha == 0:
        break
    if escolha not in [1, 2, 3]:
        print("Opção inválida! Tente novamente.")
        continue
        
    jogada_usuario = opcoes[escolha - 1]
    jogada_cpu = random.choice(opcoes)
    
    print(f"\nVocê jogou: {jogada_usuario}")
    print(f"Computador jogou: {jogada_cpu}")
    
    if jogada_usuario == jogada_cpu:
        print(">> Resultado: EMPATE!")
        empates += 1
    elif (jogada_usuario == "Pedra" and jogada_cpu == "Tesoura") or \
         (jogada_usuario == "Papel" and jogada_cpu == "Pedra") or \
         (jogada_usuario == "Tesoura" and jogada_cpu == "Papel"):
        print(">> Resultado: VOCÊ VENCEU!")
        vitorias_jogador += 1
    else:
        print(">> Resultado: COMPUTADOR VENCEU!")
        vitorias_computador += 1

print("\n=== PLACAR FINAL ===")
print(f"Suas Vitórias: {vitorias_jogador}")
print(f"Vitórias do Computador: {vitorias_computador}")
print(f"Empates: {empates}")
```
