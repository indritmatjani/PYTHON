print("MEDIA VOTI")
somma = 0
i = 0

voto = int(input("Inserire voto: "))
if voto>=0:
    while voto>=0 and voto<=30:
        somma+=voto
        i=i+1
        voto = int(input("Inserire voto: "))
    print("La somma dei voti è pari a " ,somma)
    print("La media dei voti è pari a ",float(somma)/i)
else:
    print("Voto non valido")
