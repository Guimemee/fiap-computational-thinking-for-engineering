clientes = {'nome': [], 'endereco': [], 'telefone': [], 'email': []}

while True:
    clientes['nome'].append(input("Nome:"))
    clientes['endereco'].append(input("Endereco:"))
    clientes['telefone'].append(input("Telefone:"))
    clientes['email'].append(input("Email:"))
    fim_cadastro = input("Deseja cadastrar novo cliente [S/N]?").upper()
    if fim_cadastro == "N":
        break
    elif fim_cadastro != "S":
        while True:
            print("Digite apenas S para sim ou N para não!")
            fim_cadastro = input("Deseja cadastrar novo cliente [S/N]?").upper()
            if fim_cadastro == "N" or fim_cadastro == "S":
                break
    if fim_cadastro == "N":
        break
    print()

print()
lista_nome = clientes['nome']
lista_end = clientes['endereco']
lista_tel = clientes['telefone']
lista_email = clientes['email']

for dado in range(len(lista_nome)):
    print(f"Nome:{lista_nome[dado]}")
    print(f"Endereço:{lista_end[dado]}")
    print(f"Telefone:{lista_tel[dado]}")
    print(f"E-mail:{lista_email[dado]}")
    print()
