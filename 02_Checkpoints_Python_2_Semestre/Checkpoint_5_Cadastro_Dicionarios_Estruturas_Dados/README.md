# Checkpoint 5: Sistema de Cadastro com Dicionários e Listas

> Implementar um sistema de gerenciamento e cadastro de produtos em Python utilizando Dicionários e Listas (`dict` e `list`).
> 
> **Requisitos:**
> 1. Permitir cadastrar múltiplos registros contendo: Código, Nome, Preço Unitário e Quantidade em Estoque.
> 2. Calcular automaticamente o valor patrimonial total em estoque por item (`preco * quantidade`).
> 3. Implementar rotinas de listagem geral formatada e busca indexada por código.

### Link do Código:
- 🔗 [`cadastro_versao1.py`](./cadastro_versao1.py)
- 🔗 [`cadastro_versao2.py`](./cadastro_versao2.py)

### Resolução:
```python
# Checkpoint 5 - Sistema de Cadastro com Dicionários e Listas Aninhadas

banco_dados = []

def cadastrar_produto():
    print("\n--- NOVO CADASTRO DE PRODUTO ---")
    codigo = int(input("Código do Produto: "))
    nome = input("Nome/Descrição: ")
    preco = float(input("Preço Unitário (R$): "))
    quantidade = int(input("Quantidade em Estoque: "))
    
    produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "valor_total_estoque": preco * quantidade
    }
    banco_dados.append(produto)
    print(">> Produto cadastrado com sucesso!")

def listar_produtos():
    print("\n--- RELATÓRIO DE ESTOQUE ---")
    if not banco_dados:
        print("Nenhum produto cadastrado.")
        return
    for p in banco_dados:
        print(f"Cód: {p['codigo']} | Nome: {p['nome']} | Preço: R$ {p['preco']:.2f} | Qtd: {p['quantidade']} | Total: R$ {p['valor_total_estoque']:.2f}")

def buscar_produto():
    cod = int(input("\nDigite o código do produto para busca: "))
    for p in banco_dados:
        if p['codigo'] == cod:
            print(f">> Encontrado: {p['nome']} - R$ {p['preco']:.2f} (Estoque: {p['quantidade']})")
            return
    print(">> Produto não encontrado!")

while True:
    print("\n=== SISTEMA DE GESTÃO DE ESTOQUE ===")
    print("1 - Cadastrar Produto")
    print("2 - Listar Todos os Produtos")
    print("3 - Buscar Produto por Código")
    print("0 - Sair")
    
    opcao = input("Opção: ")
    if opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        listar_produtos()
    elif opcao == '3':
        buscar_produto()
    elif opcao == '0':
        break
    else:
        print("Opção inválida!")
```
