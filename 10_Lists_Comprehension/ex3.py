# Scrivi un programma che analizza i dati di vendita di prodotti utilizzando
# dictionary comprehension e comprehension annidate. Il programma deve:
# 1. Creare un dizionario con dati di vendita di prodotti (nome prodotto come chiave
# e lista di vendite mensili come valore)
# 2. Utilizzare dictionary comprehension per creare un nuovo dizionario con il
# totale delle vendite per ogni prodotto
# 3. Utilizzare dictionary comprehension per creare un dizionario con i prodotti
# che hanno vendite totali superiori a una soglia specificata
# 4. Creare una comprehension annidata per trasformare i dati di vendita in
# un dizionario dove ogni prodotto ha le vendite categorizzate come "basse",
# "medie" o "alte" (basandosi sulla media delle vendite del prodotto)
# 5. Stampare tutti i risultati in formato leggibile
def media(valori):
    return sum(valori)/len(valori)

SOGLIA = 5000
vendite = {
    "Laptop": [1200, 1500, 1100, 1800, 1600, 2000],
    "Smartphone": [2500, 2800, 2300, 3100, 2900, 3500],
    "Tablet": [800, 950, 700, 1100, 900, 1200],
    "Monitor": [450, 600, 500, 750, 650, 800],
    "Tastiera": [150, 200, 180, 250, 220, 300],
    "Mouse": [80, 120, 100, 150, 130, 180]
}

vendite_totali = {
    prodotto:sum(valori) for prodotto, valori in vendite.items()
}
print(vendite_totali)

vendite_filtrate = {
    prodotto:sum(valori) for prodotto, valori in vendite.items() if sum(valori) > SOGLIA
}
print(vendite_filtrate)

vendite_annidate = {
    prodotto: {
        val: (
            "bassa" if val < media(valori)
            else "alta" if val > media(valori)
            else "media"
        )
        for val in valori
    }
    for prodotto, valori in vendite.items()
}
print(vendite_annidate)