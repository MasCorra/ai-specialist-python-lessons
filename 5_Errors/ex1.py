# Scrivi un programma che chiede all'utente di inserire la propria età e valida l'input
# gestendo eventuali errori. Il programma deve:
# 1. Chiedere all'utente di inserire la propria età
# 2. Gestire l'errore nel caso l'utente inserisca un valore non numerico
# 3. Verificare che l'età sia un numero positivo (maggiore di 0)
# 4. Verificare che l'età sia realistica (minore di 120)
# 5. Se tutti i controlli sono superati, stampare un messaggio di conferma con l'età inserita
# 6. In caso di errore, mostrare un messaggio appropriato e chiedere di riprovare
try:
    eta = int(input("Inserire la propria età:"))

except ValueError as error:
    print("errore di valore: il valore inserito non è valido, riprovare")
    print(error)
else:
    if 120 > eta > 0:
        print("L'età è stata inserita correttamente:", eta, "anni")
    else:
        print("L'età inserita non è corretta")