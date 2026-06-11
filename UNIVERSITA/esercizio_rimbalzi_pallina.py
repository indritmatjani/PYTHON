print("RIMBALZI PALLINA")
h=0.0
i=0

while h<=1:
    h = float(input("inserire altezza da cui viene lasciata la pallina in cm (h>1): "))
while h>1:
    h*=0.8
    i=i+1
    print("Rimbalzo n.",i," - altezza in cm: ",h)
print("il numero di rimbalzi è pari a ",i)
print("l'altezza finale è pari a" ,h,"cm")
