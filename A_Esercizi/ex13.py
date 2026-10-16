# Definisci tre risultati di tiri al bersaglio in una lista [8, 10, 7].
# Chiedi il risultato di un quarto tiro, compreso tra 0 e 10.
# Se valido, aggiungilo, elimina un solo punteggio più basso e calcola la media dei tre rimasti.
# Se la media è almeno 8, stampa "Obiettivo raggiunto".

lista = [8, 10, 5]
try:
    risultato = int(input("Inserire il risultato del quarto tiro: "))
except ValueError as error:
    print("Il valore inserito non è valido")
    print(error)
else:
    lista.append(risultato)
    lista.remove(min(lista))
    media = sum(lista) / len(lista)
    if media >= 8:
        print("Obiettivo raggiunto")
    else:
        print(media)
