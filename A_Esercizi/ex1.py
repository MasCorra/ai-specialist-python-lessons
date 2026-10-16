# Un visitatore inserisce nome e città.
# Normalizza gli spazi esterni,
# crea il badge come NOME-CITTÀ tutto maiuscolo e
# mostra quanti caratteri ha il badge senza contare il trattino.
# Se il nome o la città sono vuoti, stampa un avviso.

nome = input('Inserisci il tuo nome: ').strip().upper()
citta = input('Inserisci la citta: ').strip().upper()
badge = nome + '-' + citta
print(badge)
num_nome = len(nome)
num_citta = len(citta)
print('la lunghezza del nome è di',num_nome,'quello della citta e di',num_citta)
if not num_nome or not num_citta:
    print('Il nome o la citta non sono stati inseriti')