# Chiedi un codice che deve iniziare con LAB- e contenere almeno 8 caratteri.
# Dopo aver tolto gli spazi esterni, se entrambe le condizioni sono rispettate
# stampa la parte successiva al prefisso in maiuscolo;
# altrimenti segnala un codice non accettato. Non usare cicli.

codice=input('Inserire un codice che inizi con LAB- e contenga almeno 8 caratteri: ').strip()
index = codice.find('-')
if codice[0:index] == 'LAB' and len(codice[index+1:]) >= 8:
    upp = codice[index+1:].upper()
    print(upp)
else:
    print('Il codice non è accettato')