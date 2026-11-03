# Scrivi un programma che simula il conto alla rovescia di un razzo. Il programma deve:
# 1. Chiedere all’utente da quale numero iniziare il conto alla rovescia
# 2. Stampare ogni numero da quel valore fino a 0 usando un ciclo
# 3. Stampare “Decollo!” alla fine


valore = int(input("Inserire un valore: "))

for i in range(valore,0, -1):
    print(i)

print("Decollo!")