#Scrivi un programma che analizzi le vendite di un negozio utilizzando Pandas DataFrame e Series. Il programma deve:
#1.  Creare un DataFrame con almeno 10 vendite e le colonne prodotto, prezzo, quantita e mese. Usare i mesi “Gennaio”, “Febbraio” e “Marzo”, facendo comparire alcuni prodotti in più mesi.
#2.  Aggiungere la colonna totale_vendita, ottenuta moltiplicando prezzo per quantita.
#3.  Raggruppare le vendite per prodotto e ottenere una Series con il fatturato totale di ciascun prodotto.
#4.  Raggruppare le vendite per mese e ottenere una seconda Series con il fatturato mensile. Visualizzare i mesi nell’ordine Gennaio, Febbraio, Marzo.
#5.  Mostrare il prodotto e il mese con il fatturato maggiore usando ordinamento decrescente e head(1). Calcolare anche fatturato totale del negozio e fatturato medio per prodotto.
#6.  Classificare il fatturato totale di ogni prodotto rispetto alla media: sotto l’80% = “Basso”; sopra il 120% = “Alto”; negli altri casi = “Medio”. Usare una funzione e apply().
#7.  Filtrare il DataFrame per mostrare soltanto le vendite dei prodotti classificati come “Alto”.
#8.  Stampare i risultati in modo leggibile.

import pandas as pd

def classifica(totale_vendita):
    if totale_vendita < media_fatturato_prodotto * 0.80:
        return 'Basso'
    elif totale_vendita > media_fatturato_prodotto * 1.20:
        return 'Alto'
    else:
        return 'Medio'


#1.  Creare un DataFrame con almeno 10 vendite e le colonne prodotto, prezzo, quantita e mese.
# Usare i mesi “Gennaio”, “Febbraio” e “Marzo”, facendo comparire alcuni prodotti in più mesi.
df_vendite = pd.DataFrame({
    "prodotto": [
        "Laptop", "Mouse", "Tastiera", "Monitor",
        "Laptop", "Mouse", "Smartphone", "Tastiera",
        "Monitor", "Laptop", "Smartphone", "Mouse"
    ],
    "prezzo": [
        899.90, 25.50, 65.00, 249.99,
        899.90, 25.50, 699.90, 65.00,
        249.99, 899.90, 699.90, 25.50
    ],
    "quantita": [
        3, 15, 8, 5,
        5, 20, 4, 12,
        7, 2, 6, 18
    ],
    "mese": [
        "Gennaio", "Gennaio", "Gennaio", "Gennaio",
        "Febbraio", "Febbraio", "Febbraio", "Febbraio",
        "Marzo", "Marzo", "Marzo", "Marzo"
    ]
})

print(f"{' VENDITE ':=^60}")
print(df_vendite)
df_vendite_copy = df_vendite.copy()


#2.  Aggiungere la colonna totale_vendita, ottenuta moltiplicando prezzo per quantita.
print(f"{' TOTALE VENDITA ':=^60}")
df_vendite_copy['totale_vendita']= df_vendite_copy['prezzo']*df_vendite_copy['quantita']
print(df_vendite_copy)

#3.  Raggruppare le vendite per prodotto e ottenere una Series con il fatturato totale di ciascun prodotto.
print(f"{' GROUP BY PRODOTTO ':=^60}")
pd_vendite_fatturato = df_vendite_copy.groupby('prodotto')['totale_vendita'].sum()
#df_vendite_fatturato = df_vendite_copy.groupby('prodotto').agg(prodotto=('totale_vendita', 'sum'))
df_vendite_fatturato = df_vendite_copy.groupby('prodotto').agg(totale_vendita=('totale_vendita', 'sum'))
print(pd_vendite_fatturato)

#4.  Raggruppare le vendite per mese e ottenere una seconda Series con il fatturato mensile.
# Visualizzare i mesi nell’ordine Gennaio, Febbraio, Marzo.
print(f"{' GROUP BY MESE ':=^60}")
pd_vendite_mese = df_vendite_copy.groupby('mese')['totale_vendita'].sum().loc[['Gennaio', 'Febbraio', 'Marzo']]
#df_vendite_mese = df_vendite_copy.groupby('mese').agg(mese=('totale_vendita', 'sum'))
df_vendite_mese = (df_vendite_copy.groupby('mese').agg({'totale_vendita': 'sum'}).loc[['Gennaio', 'Febbraio', 'Marzo']])
print(df_vendite_mese)
print(pd_vendite_mese)

#5.  Mostrare il prodotto e il mese con il fatturato maggiore usando ordinamento decrescente e head(1).
print(f"{' FATTURATO PRODOTTO ':=^60}")
vendite_fatturato_maggiore = df_vendite_fatturato.sort_values(by='totale_vendita', ascending=False).head(1)
vendite_mese_maggiore = df_vendite_mese.sort_values(by='totale_vendita', ascending=False).head(1)
print(vendite_fatturato_maggiore)
print(f"{' FATTURATO MESE ':=^60}")
print(vendite_mese_maggiore)
print(f"{' STATISTICHE FATTURATO  ':=^60}")
#Calcolare anche fatturato totale del negozio e fatturato medio per prodotto.
fatturato_totale =  pd_vendite_fatturato.sum()
print(f"Il fatturato totale è di: {fatturato_totale:.2f} ")
media_fatturato_prodotto = pd_vendite_fatturato.mean()
print(f"il fatturato medio dei prodotti è: {media_fatturato_prodotto:.2f} ")

#6.  Classificare il fatturato totale di ogni prodotto rispetto alla media: sotto l’80% = “Basso”; sopra il 120% = “Alto”; negli altri casi = “Medio”. Usare una funzione e apply().
print(f"{' CLASSIFICAZIONE  ':=^60}")
df_vendite_fatturato['classificazione'] = df_vendite_fatturato['totale_vendita'].apply(classifica)
print(df_vendite_fatturato)
classificazione = pd_vendite_fatturato.apply(classifica)
print(classificazione)

#7.  Filtrare il DataFrame per mostrare soltanto le vendite dei prodotti classificati come “Alto”.
prodotti_alti = (classificazione == 'Alto').idex
mask = df_vendite_fatturato['prodotti']