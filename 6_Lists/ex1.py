# Scrivi un programma che gestisce una lista della spesa utilizzando le operazioni base sulle liste. Il programma deve:
# 1. Creare una lista iniziale con tre prodotti e mostrarla
# 2. Aggiungere due nuovi prodotti alla fine della lista e mostrarla
# 3. Inserire un prodotto all'inizio della lista e mostrarla
# 4. Rimuovere un prodotto specifico dalla lista e mostrarla
# 5. Ordinare la lista in ordine alfabetico e mostrarla come lista finale

lista_spesa = ['Ammorbidente', 'Uova', 'Formaggio']
print(lista_spesa)
lista_spesa.extend(['Cavolo', 'Zucca'])
print(lista_spesa)
lista_spesa.insert(0,'Cipolla')
print(lista_spesa)
prodotto_da_eliminare = input("Inserisci 1 prodotto da eliminare: ")

if prodotto_da_eliminare in lista_spesa:
    lista_spesa.remove(prodotto_da_eliminare)
else:
    print("Il prodotto non è nella lista della spesa")

#lista_spesa.remove('Uova')
print(lista_spesa)
lista_spesa.sort()
print(lista_spesa)

