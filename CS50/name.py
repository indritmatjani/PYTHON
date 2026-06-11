import sys

# This program prints the name passed as a command-line argument.
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("too few arguments, please provide a name")   
    
#condizione iniziale per verificare se è stato passato un argomento, se non lo è, stampiamo un messaggio di errore. Altrimenti, stampiamo il nome fornito come argomento.
if len(sys.argv) < 2:
    print("too few arguments, please provide a name")
elif len(sys.argv) > 2:
    print("too many arguments, only one name is expected")
else:
    print("hello, my name is", sys.argv[1])
    
