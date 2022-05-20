num_produto = 1
soma = 0

while True:
    valor_produto = float(input(f"Valor do produto {num_produto} (digite 0 para finalizar a compra) = R$ "))
    if valor_produto == 0:
        break
    num_produto += 1
    soma += valor_produto

print(f"Total da compra = R$ {soma:.2f}")
pagamento = float(input("Valor do pagamento = R$ "))
troco = pagamento - soma
print(f"Troco = R$ {troco:.2f} ")