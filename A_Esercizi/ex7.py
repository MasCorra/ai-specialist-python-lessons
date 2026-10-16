# Chiedi un testo che contiene una parentesi aperta ( e una parentesi chiusa ).
# Individua la prima ( e l’ultima ).
# Se sono presenti nell’ordine corretto, stampa il contenuto fra esse e la sua lunghezza;
# altrimenti mostra un messaggio di errore.

testo = input('Inserire un testo con una parentesi ( e una ): ')
index_aperta = testo.find('(')
index_chiusa = testo.rfind(')')

if index_aperta < index_chiusa and index_aperta != -1 and index_chiusa != -1:
    print(testo[index_aperta+1:index_chiusa])
    print(len(testo[index_aperta+1:index_chiusa]))
else:
    print('Errore, l\'ordine delle parentesi è sbagliato')
