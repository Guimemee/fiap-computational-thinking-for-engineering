# Checkpoint 2: Algoritmo de Cálculo de Médias FIAP com Descarte de Menor Nota

> Faça um programa para calcular a média final de uma disciplina.
> 
> **Variáveis de entrada solicitadas ao aluno (numéricas inteiras de 0 a 100):**
> - **1º semestre:** Checkpoint 1, Checkpoint 2, Checkpoint 3, Entregável 1, Entregável 2, Global Solutions
> - **2º semestre:** Checkpoint 1, Checkpoint 2, Checkpoint 3, Entregável 1, Entregável 2, Global Solutions
> - **Exame** (caso o aluno tenha ficado de exame)
> 
> **Observações e Regras:**
> 1. O programa deverá descartar a menor nota entre os três checkpoints em cada semestre.
> 2. `Média Challenge & Feedbacks = (Checkpoint A + Checkpoint B + Entregável 1 + Entregável 2) / 4`
> 3. `Média Semestre = Média Challenge * 0.4 + Global Solutions * 0.6`
> 4. `Média Parcial do Ano = Média 1º Semestre * 0.4 + Média 2º Semestre * 0.6`
> 5. **Critérios de Aprovação:**
>    - `>= 60`: **Aprovado** direto com a média final.
>    - `40 <= Média < 60`: **Exame**. Nota mínima para aprovação: `Nota Aprovação = 120 - Média Parcial`. Se `Exame >= Nota Aprovação`, `Média Final = (Exame + Média Parcial) / 2`.
>    - `< 40`: **Reprovado**.

### Link do Código:
- 🔗 [`ckeck2_questao_1ECB.py`](./ckeck2_questao_1ECB.py)

### Resolução:
```python
# Checkpoint 2 - Sistema de Cálculo de Médias FIAP com Descarte de Menor Nota e Exame

print("=== ENTRADA DE NOTAS DO 1º SEMESTRE ===")
cp1_1s = int(input("Checkpoint 1 do 1º semestre: "))
cp2_1s = int(input("Checkpoint 2 do 1º semestre: "))
cp3_1s = int(input("Checkpoint 3 do 1º semestre: "))
ent1_1s = int(input("Entregável 1 do 1º semestre: "))
ent2_1s = int(input("Entregável 2 do 1º semestre: "))
gs_1s = int(input("Global Solutions do 1º semestre: "))

# Descarte da menor nota entre os 3 checkpoints (1º Semestre)
cps_1s = [cp1_1s, cp2_1s, cp3_1s]
cps_1s.sort()
media_checkpoints_1s = (cps_1s[1] + cps_1s[2] + ent1_1s + ent2_1s) / 4.0
media_1s = (media_checkpoints_1s * 0.4) + (gs_1s * 0.6)

print("\n=== ENTRADA DE NOTAS DO 2º SEMESTRE ===")
cp1_2s = int(input("Checkpoint 1 do 2º semestre: "))
cp2_2s = int(input("Checkpoint 2 do 2º semestre: "))
cp3_2s = int(input("Checkpoint 3 do 2º semestre: "))
ent1_2s = int(input("Entregável 1 do 2º semestre: "))
ent2_2s = int(input("Entregável 2 do 2º semestre: "))
gs_2s = int(input("Global Solutions do 2º semestre: "))

# Descarte da menor nota entre os 3 checkpoints (2º Semestre)
cps_2s = [cp1_2s, cp2_2s, cp3_2s]
cps_2s.sort()
media_checkpoints_2s = (cps_2s[1] + cps_2s[2] + ent1_2s + ent2_2s) / 4.0
media_2s = (media_checkpoints_2s * 0.4) + (gs_2s * 0.6)

# Média Parcial do Ano
media_parcial = (media_1s * 0.4) + (media_2s * 0.6)

print("\n=== RESULTADO ACADÊMICO ===")
print(f"Média do 1º semestre = {media_1s:.0f}")
print(f"Média do 2º semestre = {media_2s:.0f}")
print(f"Média parcial do ano = {media_parcial:.0f}")

if media_parcial >= 60:
    print(f"Aprovado e sua média final é {media_parcial:.0f}")
elif media_parcial >= 40:
    print("Aluno de EXAME!")
    nota_aprovacao = 120 - media_parcial
    exame = int(input("Digite a nota obtida no Exame: "))
    print(f"Nota de exame = {exame}")
    if exame >= nota_aprovacao:
        media_final = (exame + media_parcial) / 2.0
        print(f"Aprovado com exame e sua média final é {media_final:.0f}")
    else:
        media_final = (exame + media_parcial) / 2.0
        print(f"Reprovado e sua média final é {media_final:.0f}")
else:
    print(f"Reprovado e sua média final é {media_parcial:.0f}")
```
