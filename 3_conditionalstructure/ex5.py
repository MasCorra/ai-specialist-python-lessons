# Scrivi un programma che calcoli il costo della spedizione di un pacco.
# Il programma deve:
# 1. Chiedere all'utente di inserire il peso del pacco in kg
# 2. Convertire il peso in un numero decimale
# 3. Chiedere all'utente se vuole la spedizione express (rispondendo "si" o "no")
# 4.Se il peso è fino a 2 kg, il costo è di 5 euro
# 5.Se il peso è fino a 10 kg, il costo è di 10 euro
# 6.Se il peso è fino a 30 kg, il costo è di 20 euro
# 7.Se il peso supera i 30 kg, stampare "Pacco troppo pesante"
# 8. Usando l'operatore ternario, aggiungere 7 euro al costo se la spedizione è express, altrimenti 0
# 9. Stampare il costo totale della spedizione
import sys
peso = float(input("Inserire il peso del pacco in kg: "))
if peso > 30:
    print("Pacco troppo pesante")
    sys.exit()

spedizione = input("Utilizzare spedizione express? (si/no): ").strip().lower()

if peso <= 2:
    costo = 5
elif peso <= 10:
    costo = 10
else:
    costo = 20

express = 7 if spedizione == "si" or spedizione == "sì" else 0
costo_finale = costo + express

print(f"La spedizione costa: {costo_finale:.2f} €")

