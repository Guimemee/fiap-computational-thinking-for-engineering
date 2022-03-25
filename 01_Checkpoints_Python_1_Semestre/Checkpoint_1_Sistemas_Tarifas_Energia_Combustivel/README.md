# Checkpoint 1: Tarifas de Energia e Precificação de Combustíveis

> 1-) Faça um programa que mostre seu nome completo na tela e seu RM da FIAP.
> 
> **Exemplo de Entrada:**
> `Nome: Michele Bazana de Souza`  
> `RM: 11111`  
> 
> **Exemplo de Saída:**
> `Nome: Michele Bazana de Souza`  
> `RM: 11111`

### Link do Código:
- 🔗 [`questao1CTFE(1).py`](./questao1CTFE(1).py)

### Resolução:
```python
# Questão 1 - Identificação do Estudante
nome = input("Digite seu nome completo: ")
rm = input("Digite seu RM: ")

print(f"Nome: {nome}")
print(f"RM: {rm}")
```

---

> 2-) Faça um programa para calcular o preço final da gasolina comum que chega no posto de combustível.
> 
> *"As distribuidoras de combustível compram nas refinarias a gasolina tipo A. Atendendo à legislação brasileira, a gasolina vendida nos postos deve ser misturada com etanol anidro. Desta maneira, no preço que o consumidor paga está incluído o preço de realização da Petrobras, o custo do etanol (que é definido livremente pelos seus produtores) e os custos e as margens de comercialização das distribuidoras e dos postos revendedores, bem como todos os impostos devidos."* Fonte: Petrobras
> 
> **Informações e Fórmulas:**
> - O usuário entrará com o preço por litro da gasolina tipo A na refinaria.
> - O usuário entrará com o preço por litro do etanol anidro nas usinas produtoras.
> - A gasolina tipo C (gasolina na bomba) é igual a 73% de gasolina tipo A mais 27% de etanol anidro:  
>   `valor_gasolinaC = valor_gasolinaA * 0.73 + valor_etanol_anidro * 0.27`
> - As distribuidoras impactam no custo em 5%:  
>   `valor_distribuidora = valor_gasolinaC * 0.05`
> - Tributos Federais (CIDE, PIS/PASEP, COFINS) = 20%:  
>   `valor_tributos_federais = (valor_gasolinaC + valor_distribuidora) * 0.2`
> - Custos e lucros de distribuição e revenda = 15%:  
>   `custos_lucros = (valor_gasolinaC + valor_distribuidora + valor_tributos_federais) * 0.15`
> - Imposto estadual ICMS = 25%:  
>   `icms = (valor_gasolinaC + valor_distribuidora + valor_tributos_federais + custos_lucros) * 0.25`
> - Preço final:  
>   `valor_gasolina_final = valor_gasolinaC + valor_distribuidora + valor_tributos_federais + icms + custos_lucros`

### Link do Código:
- 🔗 [`questao2CTFE_1ECB.py`](./questao2CTFE_1ECB.py)

### Resolução:
```python
# Questão 2 - Cálculo do Preço Final da Gasolina Comum (Gasolina C)
valor_gasolinaA = float(input("Digite o valor da gasolina tipo A por litro: R$ "))
valor_etanol_anidro = float(input("Digite o valor do etanol anidro por litro: R$ "))

# Mistura obrigatória: 73% Gasolina A + 27% Etanol Anidro
valor_gasolinaC = (valor_gasolinaA * 0.73) + (valor_etanol_anidro * 0.27)

# Custo da distribuidora (5%)
valor_distribuidora = valor_gasolinaC * 0.05

# Tributos Federais (CIDE, PIS/PASEP, COFINS = 20%)
valor_tributos_federais = (valor_gasolinaC + valor_distribuidora) * 0.20

# Custos e Lucros de Distribuição e Revenda (15%)
custos_lucros = (valor_gasolinaC + valor_distribuidora + valor_tributos_federais) * 0.15

# Imposto Estadual (ICMS = 25%)
icms = (valor_gasolinaC + valor_distribuidora + valor_tributos_federais + custos_lucros) * 0.25

# Preço final na bomba
valor_gasolina_final = valor_gasolinaC + valor_distribuidora + valor_tributos_federais + icms + custos_lucros

print(f"\nValor da gasolina C = R$ {valor_gasolinaC:.2f}")
print(f"Valor cobrado pela distribuidora responsável pela mistura = R$ {valor_distribuidora:.2f}")
print(f"Valor total dos tributos federais (CIDE, PIS/PASEP e COFINS) = R$ {valor_tributos_federais:.2f}")
print(f"Valor do ICMS = R$ {icms:.2f}")
print(f"Valor dos custos e lucros de distribuição e revenda = R$ {custos_lucros:.2f}")
print(f"Valor final da gasolina que chega no posto = R$ {valor_gasolina_final:.2f}")
```

---

> 3-) Todo mês é feita a leitura do medidor de energia da sua residência para saber qual o consumo em kWh. O consumo mensal é calculado pela diferença entre a leitura do mês atual e a leitura do mês anterior.
> 
> **Variáveis de entrada:**
> - Leitura anterior (kWh)
> - Leitura atual (kWh)
> 
> **Tarifas e Alíquotas:**
> - TUSD: 40,942% (`TUSD = consumo_mes * 0.40942`)
> - TE: 38,317% (`TE = consumo_mes * 0.38317`)
> - PIS/PASEP: 1,00% (`PIS/PASEP = consumo_mes * 0.01`)
> - COFINS: 4,62% (`COFINS = consumo_mes * 0.0462`)
> - CIP (Iluminação Pública): R$ 24,01 fixo
> - Total a pagar: `Total = TUSD + TE + PIS/PASEP + COFINS + CIP`

### Link do Código:
- 🔗 [`questao3CTFE(1).py`](./questao3CTFE(1).py)

### Resolução:
```python
# Questão 3 - Cálculo da Fatura de Energia Elétrica Residencial
leitura_anterior = float(input("Digite a leitura anterior (kWh): "))
leitura_atual = float(input("Digite a leitura atual (kWh): "))

consumo_mes = leitura_atual - leitura_anterior

# Alíquotas e Tarifas
tusd = consumo_mes * (40.942 / 100.0)
te = consumo_mes * (38.317 / 100.0)
pis_pasep = consumo_mes * (1.00 / 100.0)
cofins = consumo_mes * (4.62 / 100.0)
cip = 24.01

total_pagar = tusd + te + pis_pasep + cofins + cip

print(f"\nConsumo do mês (kWh) = {consumo_mes:.0f}")
print(f"TUSD = R$ {tusd:.2f}")
print(f"TE = R$ {te:.2f}")
print(f"PIS/PASEP = R$ {pis_pasep:.2f}")
print(f"COFINS = R$ {cofins:.2f}")
print(f"CIP = R$ {cip:.2f}")
print(f"Total a pagar (R$) = {total_pagar:.2f}")
```
