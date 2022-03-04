# Exercício 31: Pesquisa Demográfica da Prefeitura (Salários e Filhos)
# Enunciado:
# A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes, coletando dados sobre o salário e número de filhos. Elabore um programa em Python com as funções necessárias para ler esses dados para um número não determinado de pessoas e retornar a média de salário da população, a média do número de filhos, o maior salário e o percentual de pessoas com salário até R$350,00.

def pesquisar_habitantes():
    salarios = []
    filhos = []
    
    print("=== PESQUISA DEMOGRÁFICA MUNICIPAL ===")
    print("(Digite um salário negativo para encerrar)")
    
    while True:
        sal = float(input("Salário (R$): "))
        if sal < 0:
            break
        num_f = int(input("Número de filhos: "))
        salarios.append(sal)
        filhos.append(num_f)
        
    if not salarios:
        print("Nenhum dado cadastrado.")
        return
        
    media_salario = sum(salarios) / len(salarios)
    media_filhos = sum(filhos) / len(filhos)
    maior_salario = max(salarios)
    ate_350 = len([s for s in salarios if s <= 350.0])
    pct_ate_350 = (ate_350 / len(salarios)) * 100.0
    
    print("\n=== RESULTADOS DA PESQUISA ===")
    print(f"Média de salário: R$ {media_salario:.2f}")
    print(f"Média do número de filhos: {media_filhos:.1f}")
    print(f"Maior salário: R$ {maior_salario:.2f}")
    print(f"Percentual de pessoas com salário até R$ 350,00: {pct_ate_350:.2f}%")

pesquisar_habitantes()
