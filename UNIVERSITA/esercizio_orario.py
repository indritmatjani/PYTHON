print("CALCOLO NUOVO ORARIO")
i=0

h=-10
while h<0 or h>23:
    h= int(input("inserire il numero delle ore: "))

m=-10
while m<0 or m>59:
    m=int(input("inserire i minuti: "))

s=-10
while s<0 or s>59:
    s=int(input("inserire numero di secondi: "))


s2 = -1
while s2 <= 0:   # continua finché è zero o negativo
    s2 = int(input("Inserire secondi da sommare (maggiore di 0): "))
    if s2 <= 0:
        print("Errore: devi inserire un valore maggiore di zero!")
        
print("Orario iniziale",h,":",m,":",s)   
h_diff=s2//3600
m_diff=(s2//60)%60
s_diff=s2%60

print(h_diff)
print(m_diff)
print(s_diff)

s+=s_diff
m_diff+=s//60
s=s%60

m+=m_diff
h_diff+=m//60
m=m%60

h+=h_diff
if h>23:
    i=h//24
    h=h%24
if i>0:
    giorno="giorno +" +str(i)
else:
    giorno =""

print("Orario finale",h,":",m,":",s, giorno)   
