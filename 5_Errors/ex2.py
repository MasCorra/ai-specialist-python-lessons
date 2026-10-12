# Scrivi un programma che calcola il prezzo del biglietto del cinema
# in base al numero di biglietti acquistati. Il programma deve:
# 1. Chiedere all'utente quanti biglietti vuole acquistare
# 2. Gestire l'errore nel caso l'utente inserisca un valore non numerico
# 3. Se il numero di biglietti è maggiore di 5, applicare uno sconto del 15%
# 4. Se il numero di biglietti è compreso tra 3 e 5, applicare uno sconto del 10%
# 5. Se il numero di biglietti è minore di 3, non applicare sconti
# 6. Calcolare e mostrare il prezzo totale (prezzo singolo biglietto: 8.50 euro)
SINGLE_TICKET = 8.50
try:
    num_biglietti= int(input("Quanti biglietti vuoi acquistare? "))
except ValueError as error:
    print("errore di valore: il valore inserito non è valido, riprovare")
    print(error)
else:
    if num_biglietti <= 0:
        print("Inserire un numero valido di biglietti")
    else:
        if num_biglietti > 5:
            discount = 0.85
        elif 5 >= num_biglietti >= 3 :
            discount = 0.90
        else :
            discount = 1
        final_price = SINGLE_TICKET * num_biglietti * discount
        print("Il prezzo finale è di:", final_price)