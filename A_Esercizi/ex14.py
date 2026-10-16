# Chiedi una parola di almeno 6 caratteri, senza spazi interni.
# Se valida, costruisci una password unendo: gli ultimi 3 caratteri in maiuscolo,
# il numero totale di lettere e i primi 2 caratteri in minuscolo.
# Se contiene spazi o è troppo corta, stampa un avviso. Non utilizzare metodi non studiati.

parola = input("Inserire una parola senza spazi: ")
index = parola.find(' ')
if index == -1 and len(parola) >= 6:
    maiusc = parola[-3:].upper()
    totale = str(len(parola))
    minusc = parola[:2].lower()
    password = maiusc + totale + minusc
    print(password)

else:
    print("la parola è troppo corta o contiene spazi")