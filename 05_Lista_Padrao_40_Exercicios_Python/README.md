# Lista de 40 Exercícios de Programação em Python

> 1-) Crie um programa com uma função que receba um valor e informe se ele é positivo ou não.

### Link do Código:
- 🔗 [`exercicio_01.py`](./exercicio_01.py)

### Resolução:
```python
def eh_positivo(valor):
    """Verifica se um número é positivo."""
    return valor > 0

# Teste interativo
num = float(input("Digite um número: "))
if eh_positivo(num):
    print(f"O número {num} é positivo.")
else:
    print(f"O número {num} não é positivo.")
```

---

> 2-) Crie um programa com uma função que receba um valor e diga se é nulo ou não.

### Link do Código:
- 🔗 [`exercicio_02.py`](./exercicio_02.py)

### Resolução:
```python
def eh_nulo(valor):
    """Verifica se um número é nulo (igual a zero)."""
    return valor == 0

# Teste interativo
num = float(input("Digite um número: "))
if eh_nulo(num):
    print(f"O número {num} é nulo (zero).")
else:
    print(f"O número {num} não é nulo.")
```

---

> 3-) Crie um programa com uma função que receba três valores, 'a', 'b' e 'c', que são os coeficientes de uma equação do segundo grau e retorne o valor do delta, que é dado por 'b² - 4ac'

### Link do Código:
- 🔗 [`exercicio_03.py`](./exercicio_03.py)

### Resolução:
```python
def calcular_delta(a, b, c):
    """Calcula o discriminante delta de uma equação do 2º grau."""
    return (b ** 2) - (4 * a * c)

# Teste interativo
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = calcular_delta(a, b, c)
print(f"O discriminante Delta é: {delta}")
```

---

> 4-) Usando as 3 funções acima, crie um programa que calcula as raízes de uma equação do 2o grau: ax² + bx + c = 0. Para ela existir, o coeficiente 'a' deve ser diferente de zero. Caso o delta seja maior ou igual a zero, as raízes serão reais. Caso o delta seja negativo, as raízes serão complexas e da forma: x + iy

### Link do Código:
- 🔗 [`exercicio_04.py`](./exercicio_04.py)

### Resolução:
```python
import math

def eh_nulo(valor):
    return valor == 0

def eh_positivo(valor):
    return valor >= 0

def calcular_delta(a, b, c):
    return (b ** 2) - (4 * a * c)

def resolver_equacao_2grau(a, b, c):
    if eh_nulo(a):
        print("Erro: O coeficiente 'a' não pode ser zero para uma equação do 2º grau.")
        return
    
    delta = calcular_delta(a, b, c)
    print(f"Delta = {delta}")
    
    if eh_positivo(delta):
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Raízes reais: x1 = {x1:.4f}, x2 = {x2:.4f}")
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-delta) / (2 * a)
        print(f"Raízes complexas: x1 = {real:.4f} + {imag:.4f}i, x2 = {real:.4f} - {imag:.4f}i")

# Teste interativo
a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))
resolver_equacao_2grau(a, b, c)
```

---

> 5-) Crie um programa com uma função em linguagem python que receba 2 números e retorne o maior valor.

### Link do Código:
- 🔗 [`exercicio_05.py`](./exercicio_05.py)

### Resolução:
```python
def maior_de_dois(n1, n2):
    """Retorna o maior entre dois números."""
    if n1 > n2:
        return n1
    return n2

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print(f"O maior valor é: {maior_de_dois(n1, n2)}")
```

---

> 6-) Crie um programa com uma função em linguagem python que receba 2 números e retorne o menor valor.

### Link do Código:
- 🔗 [`exercicio_06.py`](./exercicio_06.py)

### Resolução:
```python
def menor_de_dois(n1, n2):
    """Retorna o menor entre dois números."""
    if n1 < n2:
        return n1
    return n2

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print(f"O menor valor é: {menor_de_dois(n1, n2)}")
```

---

> 7-) Crie um programa com uma função em linguagem python que receba 3 números e retorne o maior valor.

### Link do Código:
- 🔗 [`exercicio_07.py`](./exercicio_07.py)

### Resolução:
```python
def maior_de_tres(a, b, c):
    """Retorna o maior entre três números."""
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior

a = float(input("Digite o 1º número: "))
b = float(input("Digite o 2º número: "))
c = float(input("Digite o 3º número: "))
print(f"O maior valor entre os três é: {maior_de_tres(a, b, c)}")
```

---

> 8-) Crie um programa com uma função em linguagem python que receba 3 números e retorne o menor valor.

### Link do Código:
- 🔗 [`exercicio_08.py`](./exercicio_08.py)

### Resolução:
```python
def menor_de_tres(a, b, c):
    """Retorna o menor entre três números."""
    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    return menor

a = float(input("Digite o 1º número: "))
b = float(input("Digite o 2º número: "))
c = float(input("Digite o 3º número: "))
print(f"O menor valor entre os três é: {menor_de_tres(a, b, c)}")
```

---

> 9-) Crie um programa com uma função em linguagem python chamada Dado() que retorna, através de sorteio, um número de 1 até 6.

### Link do Código:
- 🔗 [`exercicio_09.py`](./exercicio_09.py)

### Resolução:
```python
import random

def Dado():
    """Retorna um número aleatório entre 1 e 6."""
    return random.randint(1, 6)

print(f"Resultado do lançamento do dado: {Dado()}")
```

---

> 10-) Use a função da questão anterior e lance o dado 1 milhão de vezes. Conte quantas vezes cada número saiu. A probabilidade deu certo? Ou seja, a porcentagem dos números foi parecida?

### Link do Código:
- 🔗 [`exercicio_10.py`](./exercicio_10.py)

### Resolução:
```python
import random

def Dado():
    return random.randint(1, 6)

total_lancamentos = 1_000_000
contadores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

print(f"Simulando {total_lancamentos:,} lançamentos de dado...")
for _ in range(total_lancamentos):
    face = Dado()
    contadores[face] += 1

print("\n=== RESULTADO DA CONTAGEM E PROBABILIDADE ===")
for face, cont in contadores.items():
    pct = (cont / total_lancamentos) * 100
    print(f"Face {face}: {cont:,} vezes ({pct:.2f}%) - Esperado teórico: ~16.67%")
```

---

> 11-) Com função, crie um programa de conversão entre as temperaturas Celsius e Farenheit. Primeiro o usuário deve escolher se vai entrar com a temperatura em Célsius ou Farenheit, depois a conversão escolhida é realizada através de comandos IF. Se C é a temperatura em Célsius e F em Farenheit, as fórmulas de conversão são: C = 5*(F-32)/9 e F = (9*C/5) + 32.

### Link do Código:
- 🔗 [`exercicio_11.py`](./exercicio_11.py)

### Resolução:
```python
def celsius_para_fahrenheit(c):
    return (9 * c / 5) + 32

def fahrenheit_para_celsius(f):
    return 5 * (f - 32) / 9

print("=== CONVERSOR DE TEMPERATURA ===")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")
op = input("Escolha a opção (1 ou 2): ")

if op == '1':
    c = float(input("Digite a temperatura em ºC: "))
    print(f"{c} ºC = {celsius_para_fahrenheit(c):.2f} ºF")
elif op == '2':
    f = float(input("Digite a temperatura em ºF: "))
    print(f"{f} ºF = {fahrenheit_para_celsius(f):.2f} ºC")
else:
    print("Opção inválida.")
```

---

> 12-) Um professor, muito legal, fez 3 provas durante um semestre mas só vai levar em conta as duas notas mais altas para calcular a média. Faça um programa em python que peça o valor das 3 notas, execute uma função que mostre como seria a média com essas 3 provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.

### Link do Código:
- 🔗 [`exercicio_12.py`](./exercicio_12.py)

### Resolução:
```python
def analisar_notas(n1, n2, n3):
    notas = [n1, n2, n3]
    notas_ordenadas = sorted(notas)
    
    media_todas = sum(notas) / 3.0
    media_duas_maiores = (notas_ordenadas[1] + notas_ordenadas[2]) / 2.0
    maior_nota = max(notas)
    menor_nota = min(notas)
    
    print(f"Média com as 3 provas: {media_todas:.2f}")
    print(f"Média com as 2 maiores notas ({notas_ordenadas[1]}, {notas_ordenadas[2]}): {media_duas_maiores:.2f}")
    print(f"Nota mais alta: {maior_nota}")
    print(f"Nota mais baixa (descartada): {menor_nota}")

n1 = float(input("Digite a Nota 1: "))
n2 = float(input("Digite a Nota 2: "))
n3 = float(input("Digite a Nota 3: "))
analisar_notas(n1, n2, n3)
```

---

> 13-) Elabore um programa em Python com uma função que acha todos os números primos até 1000. Número primo é aquele que é divisível somente por 1 e por ele mesmo.

### Link do Código:
- 🔗 [`exercicio_13.py`](./exercicio_13.py)

### Resolução:
```python
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def listar_primos_ate_1000():
    primos = [n for n in range(2, 1001) if eh_primo(n)]
    print(f"Total de números primos até 1000: {len(primos)}")
    print("Primos encontrados:")
    print(primos)

listar_primos_ate_1000()
```

---

> 14-) Elabore um programa em Python com uma função que recebe dois inteiros e retorna o MDC, máximo divisor comum.

### Link do Código:
- 🔗 [`exercicio_14.py`](./exercicio_14.py)

### Resolução:
```python
def mdc(a, b):
    """Calcula o MDC pelo Algoritmo de Euclides."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

num1 = int(input("Digite o 1º número inteiro: "))
num2 = int(input("Digite o 2º número inteiro: "))
print(f"O MDC({num1}, {num2}) é: {mdc(num1, num2)}")
```

---

> 15-) Elabore um programa em Python com uma função que ache todos os números perfeitos até 1000. Número perfeito é aquele que é a soma de seus fatores. Por exemplo, 6 é divisível por 1, 2 e 3 ao passo que 6 = 1 + 2 + 3.

### Link do Código:
- 🔗 [`exercicio_15.py`](./exercicio_15.py)

### Resolução:
```python
def eh_perfeito(n):
    if n < 2:
        return False
    fatores = [i for i in range(1, n) if n % i == 0]
    return sum(fatores) == n

def listar_perfeitos():
    perfeitos = [n for n in range(1, 1001) if eh_perfeito(n)]
    print(f"Números perfeitos até 1000: {perfeitos}")

listar_perfeitos()
```

---

> 16-) Elabore um programa em Python com uma função que receba um número e imprima ele na ordem inversa. Ou seja, se recebeu o inteiro 123, deve imprimir o inteiro 321.

### Link do Código:
- 🔗 [`exercicio_16.py`](./exercicio_16.py)

### Resolução:
```python
def inverter_numero(n):
    s = str(abs(n))
    inv = s[::-1]
    resultado = int(inv)
    return -resultado if n < 0 else resultado

num = int(input("Digite um número inteiro: "))
print(f"Número invertido: {inverter_numero(num)}")
```

---

> 17-) Elabore um programa em Python com uma função que recebe o raio de uma esfera e calcula o seu volume (v = 4/3 * Pi * R³).

### Link do Código:
- 🔗 [`exercicio_17.py`](./exercicio_17.py)

### Resolução:
```python
import math

def volume_esfera(raio):
    return (4.0 / 3.0) * math.pi * (raio ** 3)

r = float(input("Digite o raio da esfera: "))
print(f"O volume da esfera de raio {r} é: {volume_esfera(r):.4f}")
```

---

> 18-) Elabore um programa em Python com uma função que recebe as 3 notas de um aluno e uma letra. Se a letra for A o procedimento calcula a média aritmética das notas do aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2) e se for H, a sua média harmônica. A média calculada deve ser retornada.

### Link do Código:
- 🔗 [`exercicio_18.py`](./exercicio_18.py)

### Resolução:
```python
def calcular_media(n1, n2, n3, tipo):
    tipo = tipo.upper()
    if tipo == 'A':
        return (n1 + n2 + n3) / 3.0
    elif tipo == 'P':
        return ((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10.0
    elif tipo == 'H':
        return 3.0 / ((1.0 / n1) + (1.0 / n2) + (1.0 / n3))
    else:
        raise ValueError("Tipo de média inválido. Use A, P ou H.")

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
tipo = input("Tipo de Média (A - Aritmética, P - Ponderada, H - Harmônica): ")
print(f"Média calculada: {calcular_media(n1, n2, n3, tipo):.2f}")
```

---

> 19-) Elabore um programa em Python com uma função que recebe um valor inteiro e positivo e retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso contrário.

### Link do Código:
- 🔗 [`exercicio_19.py`](./exercicio_19.py)

### Resolução:
```python
def eh_primo(valor):
    if valor <= 1:
        return False
    for i in range(2, int(valor**0.5) + 1):
        if valor % i == 0:
            return False
    return True

num = int(input("Digite um número inteiro positivo: "))
print(f"É primo? {eh_primo(num)}")
```

---

> 20-) Elabore um programa em Python com uma função que recebe os valores necessários para o cálculo da fórmula de báskara e imprime as suas raízes, caso seja possível calcular.

### Link do Código:
- 🔗 [`exercicio_20.py`](./exercicio_20.py)

### Resolução:
```python
import math

def bhaskara(a, b, c):
    if a == 0:
        print("Coeficiente 'a' não pode ser 0.")
        return
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print("Não existem raízes reais para a equação (Delta < 0).")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Raiz x1 = {x1:.4f}")
        print(f"Raiz x2 = {x2:.4f}")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
bhaskara(a, b, c)
```

---

> 21-) Elabore um programa em Python com uma função que recebe o tempo de duração de um vídeo expresso em horas, minutos e segundos e retorna esse tempo em segundos.

### Link do Código:
- 🔗 [`exercicio_21.py`](./exercicio_21.py)

### Resolução:
```python
def converter_para_segundos(horas, minutos, segundos):
    return (horas * 3600) + (minutos * 60) + segundos

h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))
print(f"Tempo total em segundos: {converter_para_segundos(h, m, s)} segundos")
```

---

> 22-) Elabore um programa em Python com uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.

### Link do Código:
- 🔗 [`exercicio_22.py`](./exercicio_22.py)

### Resolução:
```python
def idade_em_dias(anos, meses, dias):
    # Considerando 1 ano = 365 dias e 1 mês = 30 dias
    return (anos * 365) + (meses * 30) + dias

a = int(input("Anos: "))
m = int(input("Meses: "))
d = int(input("Dias: "))
print(f"Idade total expressa em dias: {idade_em_dias(a, m, d)} dias")
```

---

> 23-) Elabore um programa em Python com uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito quando ele é igual a soma dos seus divisores excetuando ele próprio. (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar um valor booleano.

### Link do Código:
- 🔗 [`exercicio_23.py`](./exercicio_23.py)

### Resolução:
```python
def verificar_perfeito(num):
    if num <= 0:
        return False
    soma_divisores = sum([i for i in range(1, num) if num % i == 0])
    return soma_divisores == num

val = int(input("Digite um número: "))
print(f"O número {val} é perfeito? {verificar_perfeito(val)}")
```

---

> 24-) Elabore um programa em Python com uma função que recebe a idade de um nadador e retorna a categoria desse nadador de acordo com a tabela abaixo:
- 5 a 7 anos: Infantil A
- 8 a 10 anos: Infantil B
- 11 a 13 anos: Juvenil A
- 14 a 17 anos: Juvenil B
- Maiores de 18 anos (inclusive): Adulto

### Link do Código:
- 🔗 [`exercicio_24.py`](./exercicio_24.py)

### Resolução:
```python
def categoria_nadador(idade):
    if 5 <= idade <= 7:
        return "Infantil A"
    elif 8 <= idade <= 10:
        return "Infantil B"
    elif 11 <= idade <= 13:
        return "Juvenil A"
    elif 14 <= idade <= 17:
        return "Juvenil B"
    elif idade >= 18:
        return "Adulto"
    else:
        return "Idade abaixo da faixa permitida para competição (menor que 5 anos)"

idade = int(input("Digite a idade do nadador: "))
print(f"Categoria: {categoria_nadador(idade)}")
```

---

> 25-) Elabore um programa em Python com uma função que recebe um valor inteiro e verifica se o valor é positivo ou negativo. A função deve retornar um valor booleano.

### Link do Código:
- 🔗 [`exercicio_25.py`](./exercicio_25.py)

### Resolução:
```python
def eh_positivo(num):
    return num >= 0

val = int(input("Digite um valor inteiro: "))
print(f"É positivo (True) ou negativo (False)? {eh_positivo(val)}")
```

---

> 26-) Elabore um programa em Python com uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar. A função deve retornar um valor booleano.

### Link do Código:
- 🔗 [`exercicio_26.py`](./exercicio_26.py)

### Resolução:
```python
def eh_par(num):
    return num % 2 == 0

val = int(input("Digite um valor inteiro: "))
print(f"É par? {eh_par(val)}")
```

---

> 27-) Elabore um programa em Python com uma função que recebe a média final de um aluno e retorna o seu conceito, conforme a tabela abaixo:
- de 0,0 a 4,9: D
- de 5,0 a 6,9: C
- de 7,0 a 8,9: B
- de 9,0 a 10,0: A

### Link do Código:
- 🔗 [`exercicio_27.py`](./exercicio_27.py)

### Resolução:
```python
def obter_conceito(media):
    if 0.0 <= media <= 4.9:
        return 'D'
    elif 5.0 <= media <= 6.9:
        return 'C'
    elif 7.0 <= media <= 8.9:
        return 'B'
    elif 9.0 <= media <= 10.0:
        return 'A'
    else:
        return 'Média inválida (fora do intervalo [0.0, 10.0])'

media = float(input("Digite a média final do aluno: "))
print(f"Conceito atribuído: {obter_conceito(media)}")
```

---

> 28-) Elabore um programa em Python com uma função que recebe a altura (alt) e o sexo de uma pessoa e retorna o seu peso ideal. Para homens, calcular o peso ideal usando a fórmula peso ideal = 72.7 x alt - 58 e, para mulheres, peso ideal = 62.1 x alt - 44.7.

### Link do Código:
- 🔗 [`exercicio_28.py`](./exercicio_28.py)

### Resolução:
```python
def peso_ideal(altura, sexo):
    sexo = sexo.strip().upper()
    if sexo == 'M':
        return (72.7 * altura) - 58.0
    elif sexo == 'F':
        return (62.1 * altura) - 44.7
    else:
        raise ValueError("Sexo inválido. Utilize 'M' para masculino ou 'F' para feminino.")

alt = float(input("Digite a altura em metros (ex: 1.75): "))
sexo = input("Digite o sexo (M/F): ")
print(f"Peso ideal calculado: {peso_ideal(alt, sexo):.2f} kg")
```

---

> 29-) Elabore um programa em Python com uma função que recebe a hora de inicio e a hora de término de um jogo, ambas subdivididas em 2 valores distintos: horas e minutos. O procedimento deve retornar a duração do jogo em minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que o jogo pode começar em um dia e terminar no outro.

### Link do Código:
- 🔗 [`exercicio_29.py`](./exercicio_29.py)

### Resolução:
```python
def duracao_jogo_minutos(h_ini, m_ini, h_fim, m_fim):
    minutos_inicio = (h_ini * 60) + m_ini
    minutos_fim = (h_fim * 60) + m_fim
    
    if minutos_fim >= minutos_inicio:
        duracao = minutos_fim - minutos_inicio
    else:
        duracao = (24 * 60 - minutos_inicio) + minutos_fim
    return duracao

h1 = int(input("Hora de início: "))
m1 = int(input("Minuto de início: "))
h2 = int(input("Hora de término: "))
m2 = int(input("Minuto de término: "))

duracao = duracao_jogo_minutos(h1, m1, h2, m2)
print(f"Duração total do jogo: {duracao} minutos ({duracao // 60}h {duracao % 60}min)")
```

---

> 30-) Elabore um programa em Python com uma função que recebes 3 valores reais X, Y e Z e que verifique se esses valores podem ser os comprimentos dos lados de um triângulo e, neste caso, retornar qual o tipo de triângulo formado. Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade seja satisfeita: o comprimento de cada lado de um triângulo é menor do que a soma do comprimento dos outros dois lados. O procedimento deve identificar o tipo de triângulo formado: Equilátero (3 lados iguais), Isósceles (2 lados iguais), Escaleno (3 lados diferentes).

### Link do Código:
- 🔗 [`exercicio_30.py`](./exercicio_30.py)

### Resolução:
```python
def classificar_triangulo(x, y, z):
    # Validação da Desigualdade Triangular
    if (x < y + z) and (y < x + z) and (z < x + y):
        if x == y == z:
            return "Triângulo Equilátero"
        elif x == y or x == z or y == z:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "Os lados informados não formam um triângulo."

x = float(input("Lado X: "))
y = float(input("Lado Y: "))
z = float(input("Lado Z: "))
print(f"Classificação: {classificar_triangulo(x, y, z)}")
```

---

> 31-) A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes, coletando dados sobre o salário e número de filhos. Elabore um programa em Python com as funções necessárias para ler esses dados para um número não determinado de pessoas e retornar a média de salário da população, a média do número de filhos, o maior salário e o percentual de pessoas com salário até R$350,00.

### Link do Código:
- 🔗 [`exercicio_31.py`](./exercicio_31.py)

### Resolução:
```python
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
```

---

> 32-) Elabore um programa em Python com uma função que leia um número não determinado de valores positivos e retorna a média aritmética dos mesmos.

### Link do Código:
- 🔗 [`exercicio_32.py`](./exercicio_32.py)

### Resolução:
```python
def media_positivos():
    valores = []
    print("Digite valores positivos (digite um número negativo para finalizar):")
    while True:
        v = float(input("Valor: "))
        if v < 0:
            break
        valores.append(v)
    if valores:
        return sum(valores) / len(valores)
    return 0.0

m = media_positivos()
print(f"Média aritmética dos valores positivos: {m:.2f}")
```

---

> 33-) Elabore um programa em Python com uma função que receba um valor inteiro e positivo e calcula o seu fatorial.

### Link do Código:
- 🔗 [`exercicio_33.py`](./exercicio_33.py)

### Resolução:
```python
def fatorial(n):
    if n < 0:
        raise ValueError("O fatorial não é definido para números negativos.")
    fat = 1
    for i in range(2, n + 1):
        fat *= i
    return fat

num = int(input("Digite um número inteiro positivo: "))
print(f"{num}! = {fatorial(num)}")
```

---

> 34-) Elabore um programa em Python com uma função que lê 50 valores inteiros e retorna o maior e o menor deles.

### Link do Código:
- 🔗 [`exercicio_34.py`](./exercicio_34.py)

### Resolução:
```python
def maior_menor_50(lista_valores=None):
    if lista_valores is None:
        lista_valores = []
        print("Digite 50 valores inteiros:")
        for i in range(50):
            val = int(input(f"Valor {i+1}/50: "))
            lista_valores.append(val)
    return max(lista_valores), min(lista_valores)

# Exemplo com conjunto demonstrativo
amostra = list(range(1, 51))
maior, menor = maior_menor_50(amostra)
print(f"Maior valor: {maior} | Menor valor: {menor}")
```

---

> 35-) Elabore um programa em Python com uma função que recebe um valor N e calcula e escreve a tabuada de 1 até N.

### Link do Código:
- 🔗 [`exercicio_35.py`](./exercicio_35.py)

### Resolução:
```python
def tabuada_ate_n(n):
    print(f"=== TABUADA DE 1 ATÉ {n} ===")
    for i in range(1, n + 1):
        print(f"{i} x {n} = {i * n}")

n = int(input("Digite o valor de N: "))
tabuada_ate_n(n)
```

---

> 36-) Elabore um programa em Python com uma função que recebe um valor inteiro e positivo e retorna o número de divisores desse valor.

### Link do Código:
- 🔗 [`exercicio_36.py`](./exercicio_36.py)

### Resolução:
```python
def contar_divisores(n):
    if n <= 0:
        return 0
    divisores = [i for i in range(1, n + 1) if n % i == 0]
    return len(divisores)

val = int(input("Digite um valor inteiro positivo: "))
print(f"O número {val} possui {contar_divisores(val)} divisores.")
```

---

> 37-) Elabore um programa em Python com uma função que recebe um valor inteiro e positivo e retorna o somatório desse valor (1 + 2 + ... + N).

### Link do Código:
- 🔗 [`exercicio_37.py`](./exercicio_37.py)

### Resolução:
```python
def somatorio(n):
    if n <= 0:
        return 0
    return (n * (n + 1)) // 2

val = int(input("Digite um valor inteiro positivo N: "))
print(f"O somatório de 1 até {val} é: {somatorio(val)}")
```

---

> 38-) Elabore um programa em Python com uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N.

### Link do Código:
- 🔗 [`exercicio_38.py`](./exercicio_38.py)

### Resolução:
```python
def calcular_serie_harmonica(n):
    if n <= 0:
        return 0.0
    s = sum(1.0 / i for i in range(1, n + 1))
    return s

n = int(input("Digite N para o cálculo de S: "))
print(f"S = {calcular_serie_harmonica(n):.6f}")
```

---

> 39-) Elabore um programa em Python com uma função que recebe um valor inteiro e positivo N e retorna o valor de S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N! (Aproximação do número de Euler e).

### Link do Código:
- 🔗 [`exercicio_39.py`](./exercicio_39.py)

### Resolução:
```python
import math

def calcular_serie_e(n):
    if n <= 0:
        return 1.0
    s = 1.0 + sum(1.0 / math.factorial(i) for i in range(1, n + 1))
    return s

n = int(input("Digite N para aproximação da série de Euler: "))
print(f"S = {calcular_serie_e(n):.8f}")
```

---

> 40-) Elabore um programa em Python com uma função que recebe dois valores X e Z e calcula e retorna X elevado a Z sem utilizar funções ou operadores de potência prontos.

### Link do Código:
- 🔗 [`exercicio_40.py`](./exercicio_40.py)

### Resolução:
```python
def potencia_manual(x, z):
    if z == 0:
        return 1.0
    resultado = 1.0
    expoente_positivo = abs(z)
    for _ in range(expoente_positivo):
        resultado *= x
    if z < 0:
        return 1.0 / resultado
    return resultado

x = float(input("Digite a base X: "))
z = int(input("Digite o expoente Z (inteiro): "))
print(f"{x}^{z} = {potencia_manual(x, z)}")
```

---

