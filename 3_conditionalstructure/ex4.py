# Scrivi un programma che determina il costo di un biglietto del cinema in base all'età e al giorno della settimana. Il programma deve:
# 1. Chiedere all'utente di inserire l'età
# 2. Chiedere all'utente di inserire il giorno della settimana
# 3. Applicare il prezzo base di 10 euro
# 4. Se l'età è minore di 12 anni o maggiore di 65 anni, applicare uno sconto del 50%
# 5. Se il giorno è mercoledì, applicare un ulteriore sconto di 2 euro
# 6. Calcolare e stampare il prezzo finale del biglietto

eta = int(input("Inserire l'età: "))
giorno = str(input("Inserire il giorno della settimana: ")).strip().lower()
prezzo =  10
if eta < 12 or eta > 65:
    prezzo_finale= prezzo/2
else:
    prezzo_finale= prezzo
if (giorno == 'mercoledi'):
    prezzo_finale=prezzo_finale -2
else:
    prezzo_finale=prezzo_finale
print("Il biglietto costa:", prezzo_finale)