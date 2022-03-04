
a = 1
b = 1

print("Quantos valores você deseja na série?")
x=input()  
x=int(x)

print("Série de Fibonacci:")

for y in range (0,x,1):
    print("\n",a)
    c = a + b
    a = b
    b = c
    
