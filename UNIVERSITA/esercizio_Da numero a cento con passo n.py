print("Da numero a cento con passo n")
num=100
incr=-1
while incr<0 or incr>100:
    incr=int(input("Inserire valore incremento: "))
while num>100-incr:
    num=int(input("Inserire valore del numero< "+str(100-incr)+": "))
i=0
while num<100:
    num+=incr
    i+=1
print("per arrivare o superare 100, sono necessari ",i, "somme con",incr)
