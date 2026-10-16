# Scrivi un programma che cerca la prima parola in una lista
# che inizia con una sequenza specificata dall'utente.
# Il programma deve:
# 1. Creare una lista contenente almeno 10 nomi di città italiane
# 2. Chiedere all'utente di inserire una sequenza di lettere
# iniziali da cercare
# 3. Cercare nella lista la prima città che inizia con
# la sequenza inserita (ignorando maiuscole/minuscole)
# 4. Fermarsi non appena viene trovata la prima corrispondenza
# 5. Stampare la città trovata e la sua posizione nella lista
# 6. Se nessuna città corrisponde alla ricerca, mostrare un messaggio

citta = ['Roma', 'Torino', 'Milano', 'Venezia', 'Como', 'Empoli', 'Teramo', 'Firenze', 'Pinerolo', 'Moncalieri']
iniziali = input("Inserire almeno le prime 2 lettere per la ricerca").title()
for i in citta:
    if i.startswith(iniziali):
        print(i)
        print('la città:', i,'è in posizione', citta.index(i), 'nella lista')
        break
else:
    print('Non è stata trovata nessuna citta')

