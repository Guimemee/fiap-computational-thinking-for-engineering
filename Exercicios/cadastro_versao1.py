nome = []
endereco = []
telefone = []
email = []

while True:
    nome.append(input("Nome:"))
    endereco.append(input("Endereço:"))
    telefone.append(input("Telefone:"))
    email.append(input("E-mail:"))
    fim_cadastro = input("Deseja cadastrar novo cliente[S/N]?").upper()
    if fim_cadastro == "N":
        break
    elif fim_cadastro != "S":
        while True:
            print("Digite apensa S para sim ou N para não!")
            fim_cadastro = input("Deseja cadastrar novo cliente [S/N]?").upper()
            if fim_cadastro == "N" or fim_cadastro == "S":
                break
    if fim_cadastro == "N":
        break
    print()

print()
x = 0
while x < len(nome):
    print(f"Nome:{nome[x]}")
    print(f"Endereço:{endereco[x]}")
    print(f"Telefone:{telefone[x]}")
    print(f"E-mail:{email[x]}")
    x += 1
    print()