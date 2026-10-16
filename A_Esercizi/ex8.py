# Tre oggetti pesano [1.5, 2.2, 0.8] kg. 
# Chiedi il peso di un quarto oggetto. 
# Se negativo o non numerico, segnala l’errore. Altrimenti aggiungilo alla lista. 
# Se il totale supera 6 kg, 
# elimina l’ultimo oggetto aggiunto e indica il peso che eccedeva il limite; 
# poi stampa la lista definitiva e il peso finale.

pesi = [1.5, 2.2, 0.8]
try:
    peso = float(input('Inserisci un peso: '))
except ValueError as error:
    print("errore di valore: il valore inserito non è valido!")
    print(error)
else:
    if peso < 0:
        print('Errore: il peso non puo essere negativo')
    else:
        pesi.append(peso)
    if sum(pesi) > 6:
        eccesso= sum(pesi) - 6
        pesi.remove(peso)
        print('Il peso era in eccesso di:', eccesso)
    print('Il peso totale è di:', sum(pesi))
    
    