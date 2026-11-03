#Esercizio 1  |  Analisi delle valutazioni
#Scrivi un programma che analizzi le valutazioni di alcuni prodotti utilizzando una Pandas Series. Il programma deve:
#1.  Creare una Series con le valutazioni di almeno 6 prodotti, usando il nome del prodotto come indice. Inserire almeno due valori mancanti (None).
#2.  Individuare e stampare i prodotti privi di valutazione con i metodi di Pandas.
#3.  Calcolare valutazione media, massima e minima, ignorando i dati mancanti.
#4.  Sostituire i dati mancanti con la media, senza modificare la Series originale.
#5.  Creare una nuova Series di etichette: valutazione < 3.0 = “Insufficiente”; da 3.0 (incluso) a 4.0 (escluso) = “Sufficiente”; da 4.0 in poi = “Ottimo”.
#6.  Stampare i risultati in modo leggibile.
import pandas as pd

def classifica_valutazioni(voto):
    if voto < 3.0:
        return "Insufficiente"
    elif 3<=voto<4.0:
        return "Sufficiente"
    else:
        return "Ottimo"


prodotti = {
    'Telefono': 4,
    'Phon': None,
    'Cuffie': 3,
    'Piastra': None,
    'Microonde': 5,
    'Planetaria': 4
}
prodotti_series = pd.Series(prodotti, name = 'Prodotti')
print(prodotti_series)
print(prodotti_series[prodotti_series.isna()])
media_prodotti = prodotti_series.mean()
print('Media prodotti:', media_prodotti)
max_prodotti = prodotti_series.max()
print('Massimo prodotti:', max_prodotti)
min_prodotti = prodotti_series.min()
print('Minimo prodotti:',min_prodotti)
copia_prodotti= prodotti_series.copy()
print('Solo prodotti con valutazioni:')
print(copia_prodotti.dropna())
print('Valutazioni mancanti sostituite da media')
print(copia_prodotti.fillna(media_prodotti),round(2))
etichette = copia_prodotti.apply(classifica_valutazioni)
etichetti = copia_prodotti.apply(lambda valutazione: 'Insufficiente' if valutazione < 3 else 'Sufficiente' if valutazione < 4 else 'Ottimo')

print(etichetti)






