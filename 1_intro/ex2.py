pizza_price = 40
drink_price = 20
sweet_price = 20
total_price = pizza_price + drink_price + sweet_price
print("Prezzo totale: " + str(total_price) +  "€")


friends_number = int(input("Inserisci il numero di amici presenti: "))
single_price = total_price / friends_number
single_price = round(single_price, 2)
print("Il conto a persona è di: " + str(single_price) + "€")