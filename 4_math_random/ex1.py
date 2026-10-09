# Scrivi un programma che simula il lancio di due dadi. Il programma deve:
# 1. Generare casualmente il risultato del primo dado
# 2. Generare casualmente il risultato del secondo dado
# 3. Mostrare il risultato di entrambi i dadi
# 4. Calcolare e mostrare la somma dei due risultati
# 5. Determinare se la somma ottenuta è pari o dispari e stampare il risultato
import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print("I dadi han mostrato i numeri:", dice1, "e",dice2)
result = dice1 + dice2
print("La somma dei dadi è:", result)
if result % 2:
    print("La somma dei dadi è dispari")
else:
    print("La somma dei dadi è pari")

print(f"La somma è {"pari" if result%2 == 0 else "dispari"}")