# Un laboratorio registra in una matrice i risultati di quattro controlli su tre macchine.
# Ogni numero è il punteggio ottenuto in un controllo:
# controlli = [[8, 3, 6], [5, 9, 2], [7, 4, 8], [6, 1, 9]]
# Scrivi un programma che:
# 1. Visiti tutti i numeri con due cicli for annidati, senza modificare la matrice.
# 2. Calcoli e stampi la somma complessiva dei punteggi.
# 3. Per ogni riga, conti quanti valori sono almeno 6 e stampi il numero della riga (a partire da 1) e il conteggio.
# 4. Conti quante righe hanno almeno due valori >= 6.
# 5. Individui la prima riga che contiene un valore pari a 1, stampi riga e posizione
# (entrambe a partire da 1) e interrompa la ricerca appena trovato.
# 6. Se nessun valore è 1, stampi «Nessuna anomalia».
controlli = [[8, 3, 6],
             [5, 9, 2],
             [7, 4, 8],
             [6, 1, 9]]
for i in controlli:
    for j in i:
        print(j, end=' ')
    print()
somma=0
for i in controlli:
    for j in i:
        somma= somma + j
print("la somma complessiva è di: ", somma)

numero_riga = 0
righe_valide = 0

for i in controlli:
    numero_riga += 1
    conteggio = 0

    for j in i:
        if j >= 6:
            conteggio += 1

    print("Riga:", numero_riga, "- Valori >= 6:", conteggio)

    if conteggio >= 2:
        righe_valide += 1

print("Righe con almeno due valori >= 6:", righe_valide)

anomalia = False
for numero_riga, riga in enumerate(controlli, start=1):
    for numero_colonna, valore in enumerate(riga, start=1):
        if valore == 1:
            print("Anomalia trovata!")
            print("Riga:", numero_riga)
            print("Colonna:", numero_colonna)
            anomalia = True
            break

    if anomalia:
        break
if not anomalia:
    print("Nessuna anomalia")