
print("Valor inicial:")
vi=input()  
vi=int(vi)

print("Valor final:")
vf=input()  
vf=int(vf)

print("Quadrados:")

for contador in range (vi,vf+1,1):
    X = contador * contador
    print("\t",X)
    
