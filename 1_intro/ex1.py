bread_price = 2.70
milk_price = 2.50
pasta_price = 1.98
total_price = bread_price + milk_price + pasta_price
print("Prezzo totale: " + str(total_price) +  "€")


payment_import = float(input("Inserisci l'importo pagato: "))
change = payment_import - total_price
change = round(change, 2)
print("Il resto è di: " + str(change) + "€")