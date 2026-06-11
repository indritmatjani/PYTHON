print("CONFRONTO TRA 3 NUMERI")
a = input("inserisci il primo numero --> ")
b = input("inserisci il primo numero --> ")
c = input("inserisci il primo numero --> ")
if a>b:
    if a>c :
        print("a è il maggiore: ",a)
    elif c>a:
        print("c è il maggiore: ",c)
    else:
        print("a e c sono uguali e corrispondenti al numero massimo:",a)
elif b>a:
     if b>c:
        print("b è il maggiore: ",b)
     elif c>b:
        print("c è il maggiore: ",c)
     else:
        print("b e c sono uguali e corrispondenti al numero massimo:",b)
elif a>c:
    print("a e b sono uguali e corrispondenti: ",a)
elif c>a:
    print("c è il maggiore: ",c)
else:
    print("a,b,c sono uguali e corrispondenti al numero massimo: ",a)
