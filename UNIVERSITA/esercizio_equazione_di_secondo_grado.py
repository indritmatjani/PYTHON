import math

print("RISOLUZIONE EQUAZIONE DI SECONDO GRADO")
print("sia data un'equazione di 2° grado nella forma ax^2+bc+c=0 con a<>0")

a=0

while a==0:
    a = float(input("inserire a: "))
b = float(input("inserire b: "))
c = float(input("inserire c: "))

delta = b** - 4*a*c

if abs(delta) < 0.0001:
    x1= -b/(2*a)
    print("Le soluzioni reali e coincidenti sono x1 = x2 =" ,x1)
elif delta<0:
    print("l'equazione fornisce due soluzioni non reali")
else:
    x1=(math.sqrt(delta)-b)/(2*a)
    x2=(-math.sqrt(delta)-b)/(2*a)
    print("le soluzioni reali e distinte sono:")
    print("x1 =" ,x1)
    print("x2 =" ,x2)
        
