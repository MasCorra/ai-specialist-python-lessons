# Scrivi un programma che determina il costo di un biglietto del cinema in base all'età e al giorno della settimana. Il programma deve:
# 1. Chiedere all'utente di inserire l'età
# 2. Chiedere all'utente di inserire il giorno della settimana
# 3. Applicare il prezzo base di 10 euro
# 4. Se l'età è minore di 12 anni o maggiore di 65 anni, applicare uno sconto del 50%
# 5. Se il giorno è mercoledì, applicare un ulteriore sconto di 2 euro
# 6. Calcolare e stampare il prezzo finale del biglietto

BASE_PRICE = 10
REDUCE_PRICE_PERCENTAGE = 0.5
WEDNESDAY_DISCOUNT = 2

price=BASE_PRICE

age = int(input("Inserire l'età: "))
day = str(input("Inserire il giorno della settimana: ")).strip().lower()

if age < 12 or age > 65:
    price = BASE_PRICE * REDUCE_PRICE_PERCENTAGE

    if day == "mercoledì" or day =="mercoledi":
        price = price - WEDNESDAY_DISCOUNT


print(f"Il biglietto costa: {price:.2f}€")
