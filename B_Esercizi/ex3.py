# Scrivi un programma che analizza i dati meteorologici di una settimana. Il programma deve:
# 1. Creare una lista con 7 temperature (una per ogni giorno) inserite dall’utente
# 2. Calcolare la temperatura media
# 3. Trovare e stampare la temperatura massima e minima con il relativo giorno della settimana
# 4. Contare quanti giorni sono stati sopra la media e quanti sotto
# 5. Stampare un messaggio diverso in base alla media:
# sotto 0 → “Settimana glaciale”, 0-15 → “Settimana fresca”,
# 15-25 → “Settimana mite”, sopra 25 → “Settimana calda”
import sys

giorni=['Lunedi', 'Martedi', 'Mercoledi', 'Giovedi', 'Venerdi', 'Sabato', 'Domenica']

try:
    temperature= [float(t) for t in input("Inserire il valore di 7 temperature separate da uno spazio: ").split()]
except ValueError as e:
    print("Non sono stati inseriti valori numerici")
    print(e)
    sys.exit(1)
else:
    if len(temperature) != 7:
        print("Non sono state inserite 7 temperature")
        sys.exit(0)

    media= sum(temperature)/len(temperature)
    massima = max(temperature)
    minima = min(temperature)
    giorno_massima= giorni[temperature.index(massima)]
    giorno_minima=giorni[temperature.index(minima)]
    print("La temperatura media è di:", media,"°C\nla temperatura minima è stata", giorno_minima,"di :", minima,"°C\nla temperatura massima è stata",giorno_massima,"di :", massima,"°C")

    sotto_media = [t for t in temperature if t < media]
    sopra_media = [t for t in temperature if t > media]
    print("Ci sono stati", len(sotto_media),"giorni sotto la media\nCi sono stati", len(sopra_media), "giorni sopra la media")
    if media < 0:
        print("Settimana gelida")
    elif 0<=media<15:
        print("Settimana fredda")
    elif 15<=media<25:
        print("Settimana mite")
    else:
        print("Settimana calda")