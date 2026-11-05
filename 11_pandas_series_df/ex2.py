#Scrivi un programma che gestisca un piccolo magazzino utilizzando un Pandas DataFrame. Il programma deve:
#1.  Creare un DataFrame di almeno 8 prodotti con colonne nome, categoria, prezzo, quantita, citta.
# Usare almeno 3 categorie e 3 città.
#2.  Aggiungere la colonna valore_magazzino, calcolata come prezzo × quantita.
#3.  Selezionare i soli prodotti di categoria “informatica” con prezzo > 100 €.
#4.  Ordinare i prodotti per valore_magazzino decrescente.
#5.  Raggruppare i prodotti per categoria e calcolare valore totale delle scorte, prezzo medio e quantità totale.
#6.  Aggiungere una colonna disponibilita: quantità < 5 = “Scarsa”; da 5 a 15 (inclusi) = “Media”; > 15 = “Alta”.
#7.  Stampare risultati e riepilogo in modo leggibile.
import pandas as pd


#1.  Creare un DataFrame di almeno 8 prodotti con colonne nome, categoria, prezzo, quantita, citta. Usare almeno 3 categorie e 3 città.
prodotti = pd.DataFrame({
    "nome": ["Laptop", "Mouse", "Tastiera", "Monitor", "Scrivania", "Sedia", "Smartphone", "Tablet"],
    "categoria": ["Elettronica", "Accessori", "Accessori", "Elettronica",
                  "Arredamento", "Arredamento", "Elettronica", "Elettronica"],
    "prezzo": [899.90, 25.50, 65.00, 249.99, 180.00, 120.00, 699.90, 349.90],
    "quantita": [10, 50, 30, 15, 8, 12, 20, 18],
    "citta": ["Torino", "Milano", "Roma", "Torino", "Milano", "Roma", "Torino", "Milano"]
})
df_prodotti = prodotti.copy()
print(df_prodotti)
print(f"{' VALORE MAGAZZINO ':=^60}")
#2.  Aggiungere la colonna valore_magazzino, calcolata come prezzo × quantita.
df_prodotti['valore_magazzino'] = prodotti['prezzo']*prodotti['quantita']
print(df_prodotti)
print(f"{' FILTRAGGIO ':=^60}")

#3.  Selezionare i soli prodotti di categoria “informatica” con prezzo > 100 €.
maschera = ((df_prodotti['prezzo']>100)&(df_prodotti['categoria']=='Elettronica'))
df_selezione_prodotti = df_prodotti.loc[maschera]
print(df_selezione_prodotti)
print(f"{' SORT BY ':=^60}")

#4.  Ordinare i prodotti per valore_magazzino decrescente.
df_prodotti_sort = df_prodotti.sort_values(by=['valore_magazzino','citta'], ascending=False)
print(df_prodotti_sort)
print(f"{' RIEPILOGO ':=^60}")

#5.  Raggruppare i prodotti per categoria e calcolare valore totale delle scorte, prezzo medio e quantità totale.
riepilogo = df_prodotti.groupby('categoria').agg(valore_totale=('valore_magazzino','sum'), prezzo_medio=('prezzo','mean'), quantita_totale=('quantita','sum'))
print(riepilogo)
print(f"{' DISPONIBILITA ':=^60}")

#6.  Aggiungere una colonna disponibilita: quantità < 5 = “Scarsa”; da 5 a 15 (inclusi) = “Media”; > 15 = “Alta”.
df_prodotti['disponibilita'] =df_prodotti['quantita'].apply(lambda x: 'Scarsa' if x<5 else 'Media' if x<=15 else 'Alta')
print(df_prodotti)
