# Scrivi un programma che mostra un menù di operazioni matematiche e permette all'utente
# di eseguire calcoli. Il programma deve:
# 1. Mostrare un menù con almeno 5 opzioni (es: addizione, sottrazione, moltiplicazione,
# divisione e uscita)
# 2. Chiedere all'utente di scegliere un'operazione inserendo il numero corrispondente
# 3. Se l'utente sceglie un'operazione matematica, chiedere due numeri
# 4. Eseguire l'operazione scelta e mostrare il risultato
# 5. Tornare al menù principale dopo ogni operazione
# 6. Terminare il programma quando l'utente sceglie l'opzione di uscita
opzioni = ['addizione', 'sottrazione', 'moltiplicazione', 'divisione', 'uscita']
while True:
    try:
        scelta = int(input("Inserire il numero corrispondente all'opzione scelta (1-5): "))
    except ValueError as e:
        print("Il valore inserito non è valido")
        print(e)
    else:
        if scelta>5 or scelta <1:
            print("Il numero inserito non è compreso tra 1 e 5")
            continue
        if scelta ==5:
            print("Uscita dal programma")
            break
        while True:
            try:
                numero1=int(input("Inserire il primo numero: "))
                numero2 = int(input("Inserire il secondo numero: "))
                break
            except ValueError as e:
                print("Il valore inserito non è valido")
                print(e)

        if scelta == 1:
            print("l'addizione dei due numeri vale:", numero1+numero2)
        elif scelta == 2:
            print("la sottrazione dei due numeri vale:", numero1 - numero2)
        elif scelta == 3:
            print("la moltiplicazione dei due numeri vale:", numero1 * numero2)
        elif scelta == 4:
            try:
                print("la divisione dei due numeri vale:", numero1 / numero2)
            except ZeroDivisionError as error:
                print("Il valore inserito non è valido")
                print(error)
        else:
            print("Il numero inserito non è compreso tra 1 e 5")
            scelta=1
