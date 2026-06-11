#importo la libreria random per generare numeri casuali (tutta la libreria random è disponibile in Python)
import random

#importo solo la funzione choice dalla libreria random (posso usare direttamente choice senza dover scrivere random.choice)

#from random import choice

#lanciare una moneta
coin = random.choice(["heads", "tails"])
print(f"The coin landed on {coin}.")

#numero casuale tra 1 e 10
random_number = random.randint(1, 10)
print(f"The random number is {random_number}.")

#mischiare una lista di 3 carte
cards=["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(f"The card is {card}.")
    
#statistiche libraria
import statistics

#media di una lista di numeri
voto = statistics.mean([100,90])
print(f"The average grade is {voto}.")