# Checkpoint 6 - Jogo da Forca Interativo em Python

palavra_secreta = "ENGENHARIA".upper()
letras_acertadas = ["_" for _ in palavra_secreta]
letras_erradas = []
tentativas_maximas = 6

print("=== BEM-VINDO AO JOGO DA FORCA (FIAP CTE) ===")

while True:
    print(f"\nPalavra: {' '.join(letras_acertadas)}")
    print(f"Letras erradas: {', '.join(letras_erradas)}")
    print(f"Vidas restantes: {tentativas_maximas - len(letras_erradas)}")
    
    chute = input("Digite uma letra: ").strip().upper()
    
    if len(chute) != 1 or not chute.isalpha():
        print("Por favor, digite apenas uma letra válida.")
        continue
        
    if chute in letras_acertadas or chute in letras_erradas:
        print("Você já tentou essa letra!")
        continue
        
    if chute in palavra_secreta:
        for idx, letra in enumerate(palavra_secreta):
            if letra == chute:
                letras_acertadas[idx] = chute
        print(">> Letra correta!")
    else:
        letras_erradas.append(chute)
        print(">> Letra incorreta!")
        
    if "_" not in letras_acertadas:
        print(f"\nPARABÉNS! Você acertou a palavra secreta: {palavra_secreta}")
        break
        
    if len(letras_erradas) >= tentativas_maximas:
        print(f"\nGAME OVER! Você foi enforcado. A palavra era: {palavra_secreta}")
        break
