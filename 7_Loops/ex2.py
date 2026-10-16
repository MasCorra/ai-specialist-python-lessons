# Scrivi un programma Python che conta quante cifre numeriche sono presenti in una stringa
# di testo.
# Il programma deve:
#
# 1. Chiedere all'utente un testo da analizzare
# 2. Identificare tutte le cifre (da 0 a 9) presenti nella stringa
# 3. Visualizzare ogni cifra trovata
# 4. Contare il numero totale di cifre
# 5. Visualizzare il risultato finale

# BONUS: Contare anche il numero di cifre pari

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
testo= input("Inserire un testo da analizzare")
counter=0
count_pari=0
for i in testo:
    if i in DIGITS:
        print(i)
        counter+=1
        if int(i) % 2 ==0:
            count_pari+=1
print('conta_numero', counter)
print('conta_pari', count_pari)