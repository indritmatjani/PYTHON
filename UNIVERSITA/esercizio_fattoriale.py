print("FATTORIALE")

prod=1
N=0
while N<=1:
    N = int(input("Inserire N>1: "))
for i in range(2,N+1):
    prod*=i
print("fattoriale di N è pari a" ,prod)
