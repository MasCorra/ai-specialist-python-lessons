# Chiedi un’etichetta nel formato REPARTO:ARTICOLO (per esempio CASA:LAMPADA).
# Trova i due segmenti usando find e slicing.
# Se manca : oppure uno dei due segmenti è vuoto, segnala l’errore.
# Altrimenti stampa il reparto in maiuscolo,
# l’articolo in minuscolo e il numero di caratteri complessivi delle due parti

etichetta = input("Inserire un etichetta nel formato REPARTO:ARTICOLO ")
index = etichetta.find(':')
if index == -1:
    print("Errore: formato dell'etichetta non valido, mancano i \':\'")
elif index == 0 or index +1 == len(etichetta):
    print("Errore: formato dell'etichetta non valido, manca uno dei due campi")
else:
    reparto = etichetta[:index].upper()
    articolo = etichetta[index+1:].lower()
    print(reparto)
    print("Il reparto ha:", len(reparto), "caratteri")
    print(articolo)
    print("L articolo ha:",len(articolo), "caratteri")


