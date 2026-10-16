# Definisci una lista con tre punteggi differenti.
# Sostituisci il secondo con un valore inserito dall’utente.
# Se il nuovo valore è negativo, non modificare la lista.
# Altrimenti ordina i risultati dal più alto al più basso e
# stampa primo, ultimo e differenza fra massimo e minimo.

punteggi = [ 8 , 4 , 5 ]
try:
    valore = int(input('Inserire un nuovo valore:'))
except ValueError as error:
    print("errore di valore: il valore inserito non è valido!")
    print(error)
else:
    if 0 > valore:
        print('Il valore inserito non è valido')
    else:
        punteggi[1] = valore
        punteggi.sort(reverse=True)
        print(punteggi)
        print(punteggi[0])
        print(punteggi[-1])
        differenza= max(punteggi) - min(punteggi)
        print(differenza)