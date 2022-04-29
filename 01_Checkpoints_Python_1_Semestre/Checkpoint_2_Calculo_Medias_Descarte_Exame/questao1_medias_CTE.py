check1_1 = int(input("Checkpoint 1 do 1º semestre = "))
check2_1 = int(input("Checkpoint 2 do 1º semestre = "))
check3_1 = int(input("Checkpoint 3 do 1º semestre = "))
entrega1_1 = int(input("Entregável 1 do 1º semestre = "))
entrega2_1 = int(input("Entregável 2 do 1º semestre = "))
global_solutions_1 = float(input("Global solutions do 1º semestre = "))

check1_2 = int(input("\nCheckpoint 1 do 2º semestre = "))
check2_2 = int(input("Checkpoint 2 do 2º semestre = "))
check3_2 = int(input("Checkpoint 3 do 2º semestre = "))
entrega1_2 = int(input("Entregável 1 do 2º semestre = "))
entrega2_2 = int(input("Entregável 2 do 2º semestre = "))
global_solutions_2 = int(input("Global solution do 2º semestre = "))

if check1_1 < check2_1 and check1_1 < check3_1:
    media_project1 = (check2_1 + check3_1 + entrega1_1 + entrega2_1) / 4
elif check2_1 < check1_1 and check2_1 < check3_1:
    media_project1 = (check1_1 + check3_1 + entrega1_1 + entrega2_1) / 4
else:
    media_project1 = (check1_1 + check2_1 + entrega1_1 + entrega2_1) / 4

media_semestral1 = media_project1 * 0.4 + global_solutions_1 * 0.6

if check1_2 < check2_2 and check1_2 < check3_2:
    media_project2 = (check2_2 + check3_2 + entrega2_1 + entrega2_2) / 4
elif check2_2 < check1_2 and check2_2 < check3_2:
    media_project2 = (check1_2 + check3_2 + entrega2_1 + entrega2_2) / 4
else:
    media_project2 = (check1_2 + check2_2 + entrega2_1 + entrega2_2) / 4

media_semestral2 = media_project2 * 0.4 + global_solutions_2 * 0.6

media_parcial = media_semestral1 * 0.4 + media_semestral2 * 0.6

print(f"\nMédia do 1º semestre = {media_semestral1:.0f}")
print(f"Média do 2º semestre = {media_semestral2:.0f}")
print(f"Média parcial do ano = {media_parcial:.0f}")

if media_parcial >= 60:
    media_final = media_parcial
    print(f"Aprovado e sua média final é {media_final:.0f}")
elif media_parcial >= 40:
    exame = float(input("Nota de exame = "))
    nota_aprovacao = 120 - media_parcial
    if exame >= nota_aprovacao:
        media_final = (exame + media_parcial) / 2
        print(f"Aprovado e sua média final é {media_final:.0f}")
    else:
        media_final = (exame + media_parcial) / 2
        print(f"Reprovado e sua média final é {media_final:.0f}")
else:
    print(f"Reprovado e sua média final é {media_parcial:.0f}")
