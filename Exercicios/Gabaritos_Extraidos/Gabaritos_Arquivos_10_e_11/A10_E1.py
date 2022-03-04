print("Qual é o fatorial?")
x=input()
x=int(x)

if x == 0:
    y = 1
else:
    y = x

while x>1:
    x=x-1
    y=y*x

print("Resultado: ",y)
