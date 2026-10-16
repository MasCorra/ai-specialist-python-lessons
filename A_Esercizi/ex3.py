# Chiedi una parola. Elimina gli spazi esterni e trasformala in minuscolo.
# Se ha almeno 4 caratteri, stampa i primi due, gli ultimi due e la parola al contrario;
# altrimenti stampa "Parola troppo corta". Conta quante volte compare la lettera a.

parola = input('Inserisci una parola:').strip().lower()
if len(parola) >= 4:
    print(parola[0:2])
    print(parola[-2:])
    print(parola[::-1])
else:
    print('La parola è troppo corta')

numero = parola.count('a')
print('La lettera a compare',numero,'volte' )