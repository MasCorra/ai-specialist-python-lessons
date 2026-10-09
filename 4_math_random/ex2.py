# Scrivi un programma che giochi a indovinare un numero.
# Il programma deve:
# 1. Generare casualmente un numero segreto compreso tra 1 e 20
# 2. Chiedere all'utente di inserire un numero
# 3. Convertire il numero inserito in un numero intero
# 4. Se il numero è uguale al numero segreto, stampare "Hai indovinato!"
# 5. Se la differenza tra i due numeri è al massimo 2, stampare "Ci sei quasi!"
# 6. Altrimenti, stampare se il numero segreto era più alto o più basso
# 7. Stampare il numero segreto

import random
import sys

secret_number = random.randint(1,20)
guess_number = int(input("Inserire un numero tra 1 e 20: "))
if not 1 <= guess_number <= 20:
    print("Hai inserito un numero non valido")
    sys.exit()

if guess_number == secret_number:
    print("Hai indovinato")
    sys.exit()
elif abs(guess_number - secret_number) <= 2:
    print("Ci sei quasi")
else:
    if guess_number < secret_number:
        print("Il numero segreto era piu alto")
    else:
        print("Il numero segreto era piu basso")

print("Il numero segreto era:", secret_number)