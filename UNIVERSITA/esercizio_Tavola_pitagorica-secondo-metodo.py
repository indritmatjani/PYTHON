#commento secondo modo di scrivere questo codice
print("TAVOLA PITAGORICA secondo metodo")

N = int(input("Inserire N "))

print("*" ,end="\t")
for i in range(1,N+1):
    print(i,end="\t")
print("")

for i in range(1,N*9):
    print("-",end="")
print("")

for i in range(1,N+1):
    print(i,end="\t|")
    for j in range(1,11):
        print(i*j,end="\t")
    print("")
