# Scrivi un programma che chiede all'utente di inserire due numeri e calcola la
# percentuale del primo rispetto al secondo, gestendo eventuali errori. Il programma deve:
# 1. Chiedere all'utente di inserire il primo numero (valore)
# 2. Chiedere all'utente di inserire il secondo numero (totale)
# 3. Gestire l'errore nel caso l'utente inserisca valori non numerici
# 4. Gestire l'errore nel caso il secondo numero sia zero (divisione per zero)
# 5. Calcolare la percentuale: (primo_numero / secondo_numero) * 100
# 6. Se tutti i controlli sono superati, stampare il risultato della percentuale
# 7. In caso di errore, mostrare un messaggio appropriato
try:
    valore= int(input("Inserire il primo numero: "))
    totale= int(input("Inserire il secondo numero: "))
    percent = (valore / totale) * 100
except ValueError as error:
    print("errore di valore: il valore inserito non è valido, riprovare")
    print(error)
except ZeroDivisionError:
    print("Stai dividendo per zero!")
else:
    print("Il valore percentuale del primo numero sul secondo è di:", percent)
    print(f"La percentuale calcolata è:{percent:.2f}%")
