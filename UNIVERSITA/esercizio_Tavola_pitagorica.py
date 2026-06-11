print("TAVOLA PITAGORICA")

N=int(input("Inserire N "))
for i in range(1,N+1):
    print("Tabellina del",i)
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
    print("")
   

