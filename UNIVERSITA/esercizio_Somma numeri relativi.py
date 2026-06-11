print("SOMMA NEGATIVI e POSITIVI")
pos=0
neg=0
n=int(input("Inserire numero: "))
while n!=0:
    if n>0:
        pos+=n
    elif n<0:
        neg-=n
    n=int(input("Inseire numero: "))
if pos>neg:
    print("la somma dei valori assoluti dei numeri positivi (",pos,")")
    print("è maggiore della somma dei valori assoluti dei numeri negativi (-",neg,")")
elif pos<neg:
    print("la somma dei valori assoluti dei numeri negativi (-",neg,")")
    print("è maggiore della somma dei valori assoluti dei numeri positivi(",pos,")")
else:
    print("la somma dei valori assoluti dei numeri positivi (",pos,")")
    print("è uguale alla somma dei valori assoluti dei numeri negativi (-",neg,")")
