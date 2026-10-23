# Scrivi un programma che gestisce l'inventario di un negozio di
# elettronica utilizzando un dizionario. Il programma deve:
#
# 1. Creare un dizionario con almeno 5 prodotti come chiavi e le
# relative quantità disponibili come valori
# 2. Stampare l'inventario completo mostrando ogni prodotto con la
# sua quantità
# 3. Calcolare e stampare il numero totale di articoli in
# magazzino (somma di tutte le quantità)
# 4. Trovare e stampare il prodotto con la maggiore disponibilità
# 5. Trovare e stampare il prodotto con la minore disponibilità
# 6. Aggiungere un nuovo prodotto all'inventario con la sua quantità
# 7. Aggiornare la quantità di un prodotto esistente (simulando una vendita)
# 8. Stampare l'inventario aggiornato
from idlelib.editor import keynames

# 1. Creare un dizionario con almeno 5 prodotti come chiavi e le
# relative quantità disponibili come valori
inventario = {"Computer" : 8 , "Playstation" : 5 , "Tastiera" : 15, "Monitor" : 11, "PowerBank" : 25}
somma = 0

# 2. Stampare l'inventario completo mostrando ogni prodotto con la
# sua quantità
# 3. Calcolare e stampare il numero totale di articoli in
# # magazzino (somma di tutte le quantità)
for chiave in inventario:
    print(chiave, inventario[chiave])
    somma += inventario[chiave]
print("Il totale degli articoli in inventario è: ", somma)

# 4. Trovare e stampare il prodotto con la maggiore disponibilità
massimo = 0
chiave_massimo = ""

for chiave, valore in inventario.items():
    if valore > massimo:
        chiave_massimo = chiave
        massimo = valore
print(f"Prodotto con maggior disponibilità: {chiave_massimo}, quantità: {massimo}")

# 5. Trovare e stampare il prodotto con la minore disponibilità
minimo = massimo
chiave_minimo = ""

for key, value in inventario.items():
    if value < minimo:
        chiave_minimo = key
        minimo = value
print(f"Prodotto con minor disponibilità: {chiave_minimo}, quantità: {minimo}")

# 6. Aggiungere un nuovo prodotto all'inventario con la sua quantità
new_item = input("Inserisci un nuovo prodotto: ")
quantita = int(input("Inserisci la quantità: "))
inventario.setdefault(new_item , quantita)
print("Inventario aggiornato: ", inventario)

# 7. Aggiornare la quantità di un prodotto esistente (simulando una vendita)
item_sold = input("Inserisci il nome dell'articolo venduto: ").strip().title()

try:
    quantita_prodotto = int(input("Inserisci la quantita: "))
    inventario[item_sold] -= quantita_prodotto

except ValueError:
    print("Hai inserito una quantità non corretta")
# 8. Stampare l'inventario aggiornato

print(inventario)

