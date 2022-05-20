# Checkpoint 3: Corretor de Gabarito e Caixa Registradora

> 1-) Faça um programa para verificar a nota do estudante em uma avaliação com 10 questões de múltipla escolha. O programa deve perguntar a resposta de cada questão, comparar com o gabarito da avaliação e calcular a nota total (atribuir 1 ponto para cada resposta correta).
> 
> **Gabarito Oficial:**  
> `01 - A | 02 - B | 03 - C | 04 - D | 05 - E | 06 - E | 07 - D | 08 - C | 09 - B | 10 - A`
> 
> Antes da correção o programa deverá mostrar o gabarito da avaliação na tela.

### Link do Código:
- 🔗 [`check3_1ECB_questao1.py`](./check3_1ECB_questao1.py)

### Resolução:
```python
# Checkpoint 3 - Questão 1: Verificador e Corretor Automático de Gabarito

gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

print("Gabarito da avaliação:")
for i, g in enumerate(gabarito):
    print(f"{i+1:02d} - {g}", end=" ")
print("\n")

pontuacao = 0
for i in range(10):
    resposta = input(f"Resposta da questão {i+1}: ").strip().upper()
    if resposta == gabarito[i]:
        pontuacao += 1

print(f"\nA nota total é igual a {pontuacao} ponto(s).")
```

---

> 2-) A Michele possui uma loja de conveniências e necessita de um programa que implemente uma caixa registradora.
> 
> O programa deverá receber um número desconhecido de valores referentes aos preços dos produtos. Quando o valor 0 (zero) for digitado pelo operador, a compra será finalizada.
> 
> Após a finalização da compra, o programa deve mostrar o total da compra e perguntar o pagamento que o cliente forneceu, para então calcular e mostrar o valor do troco.

### Link do Código:
- 🔗 [`check3_1ECB_questao2.py`](./check3_1ECB_questao2.py)

### Resolução:
```python
# Checkpoint 3 - Questão 2: Caixa Registradora de Loja de Conveniências

total_compra = 0.0
contador = 1

while True:
    preco = float(input(f"Valor do produto {contador} (digite 0 para finalizar a compra) = R$ "))
    if preco == 0:
        break
    total_compra += preco
    contador += 1

print(f"\nTotal da compra = R$ {total_compra:.2f}")

pagamento = float(input("Valor do pagamento = R$ "))
troco = pagamento - total_compra

print(f"Troco = R$ {troco:.2f}")
```
