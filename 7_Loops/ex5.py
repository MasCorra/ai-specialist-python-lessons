# Scrivi un programma che gestisce una lista di attività da fare (to-do list)
# con un menù interattivo. Il programma deve:
# 1. Creare una lista vuota per memorizzare le attività
# 2. Mostrare un menù con almeno 5 opzioni: visualizzare le attività,
# aggiungere un'attività, rimuovere un'attività, contare le attività e uscire
# 3. Chiedere all'utente di scegliere un'opzione dal menù
# 4. Se l'utente sceglie di visualizzare le attività, mostrare tutte le
# attività presenti con i loro indici (o un messaggio se la lista è vuota)
# 5. Se l'utente sceglie di aggiungere un'attività, chiedere il testo
# dell'attività e aggiungerla alla lista
# 6. Se l'utente sceglie di rimuovere un'attività, mostrare le attività
# con i loro indici, chiedere quale rimuovere e rimuoverla
# (gestendo eventuali errori)
# 7. Se l'utente sceglie di contare le attività, mostrare il numero
# totale di attività presenti
# 8. Ripetere il menù dopo ogni operazione finché l'utente non sceglie di uscire
# 9. Mostrare un messaggio di errore se l'utente inserisce un'opzione non valida

to_do_list =['correre', 'saltare']
opzioni=['visualizzare', 'aggiungere', 'rimuovere','contare', 'uscire']

while True:
    print('\nMENU')
    for i in opzioni:
        print(i)

    scelta = input('Scegliere un opzione tra le seguenti: ').lower().strip()

    if scelta == 'visualizzare':
        print("Visualizzazione attività:")
        if len(to_do_list)== 0:
            print('La lista è vuota')
        else:
            for indice, attivita in enumerate(to_do_list, start=1):
                print(indice, attivita)
    elif scelta== 'aggiungere':
        print("Aggiunta attività")
        attivita = input("Inserire un attività: ")
        if attivita:
            to_do_list.append(attivita)
        else:
            print("Non puoi aggiungere un attività vuota")
            continue
    elif scelta== 'rimuovere':
        if len(to_do_list)== 0:
            print('La lista è vuota')
        else:
            print("Rimozione attività")
            print("Elenco attività: ")
            for indice, attivita in enumerate(to_do_list, start=1):
                print(indice, attivita)
            while True:
                try:
                    indice = int(input("Numero dell'attività da rimuovere: "))
                except ValueError as e:
                    print("Hai inserito un valore errato")
                    print(e)
                else:
                    if 1<=indice<= len(to_do_list):
                        rimossa = to_do_list.pop(indice - 1)
                        print("Attività rimossa:", rimossa)
                        break
                    else:
                        print("Indice inserito non valido")

    elif scelta== 'contare':
        print("Conteggio attività ")
        print("Numero di attività:", len(to_do_list))
    elif scelta== 'uscire':
        print("Chiusura programma ")
        break
    else:
        print("Hai inserito un opzione non valida ")