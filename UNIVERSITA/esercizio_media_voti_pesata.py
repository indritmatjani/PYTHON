print("MEDIA VOTI PESATA")

sommav=0
sommac=0
voto=int(input("inserire il voto -> "))
if voto>=0:
    while voto>=0 and voto <=30:
        crediti = -1
        while crediti <=0:
            crediti = float(input("inserire CFU -> "))
        sommav+=voto*crediti
        sommac+=crediti
        voto = int(input("inserire voto: "))
    print("La media dei voti è pari a ",sommav/sommac)
else:
    print("voto non valido")        
