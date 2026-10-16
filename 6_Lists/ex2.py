# Scrivi un programma che gestisce le classi di una scuola e permette di modificare
# gli studenti senza alterare l'elenco originale. Il programma deve:
# 1. Creare una lista nidificata che rappresenta tre classi, ciascuna con almeno 3 nomi di studenti
# 2. Creare una copia profonda (deep copy) della lista delle classi per creare un backup
# 3. Stampare entrambe le liste (originale e backup)
# 4. Aggiungere un nuovo studente a una delle classi nella lista originale
# 5. Stampare nuovamente entrambe le liste per verificare che il backup non sia stato modificato
# 6. Mostrare un messaggio che conferma che il backup è rimasto invariato
import copy

classe1 = ['Luca', 'Mario','Ettore']
classe2 = ['Luisa', 'Alice', 'Giorgia']
classe3 = ['Maria', 'Gino', 'Luigi']
classi = [classe1, classe2, classe3]
classi_backup = copy.deepcopy(classi)
print('originale: ', classi, '\n copia:', classi_backup)

classe1.append('Gabriele')
print('originale: ', classi, '\n copia:', classi_backup)
if classi == classi_backup:
    print('Il backup è stato modificato')
else:
    print('Il backup è rimasto intatto')

