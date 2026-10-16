# Definisci una lista con tre prezzi decimali di prodotti diversi.
# Chiedi quanti euro ha a disposizione la persona. Calcola il totale;
# se basta, stampa il resto, altrimenti stampa quanti euro mancano.
# Mostra anche il prodotto più costoso e quello meno costoso.

prezzi = [8.5 , 2.4 , 7.3]
try:
    fondi = float(input('Quanti soldi hai? '))
except ValueError as error:
    print("errore di valore: il valore inserito non è valido!")
    print(error)
else:
    if fondi < 0:
        print("budget non valido")
    else:
        costi= sum(prezzi)
        if fondi >= costi:
            resto= round(fondi - costi, 2)
            print('Hai', resto,'€ di resto')
        else:
            debito= round( costi - fondi, 2)
            print('Ti mancano', debito,'€')

        print('il prodotto piu costoso vale:', max(prezzi), '€, quello meno costoso vale:', min(prezzi),'€')