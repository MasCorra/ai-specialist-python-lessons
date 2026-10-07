#Scrivi un programma che analizza un numero intero. Il programma deve:
# 1. Definire o chiedere all'utente di inserire un numero intero
# 2. Determinare e stampare se il numero è positivo, negativo o zero
# 3. Se il numero e positivo, verificare e stampare se è pari o dispari
# 4. Se il numero è positivo e pari, controllare e stampare se è maggiore di 100.


x= int(input("Inserire un numero intero: "))
if x > 0:
    print("Il numero è positivo")
    if x%2==0:
        print("Il numero è pari")
        if x > 100:
            print("Il numero è maggiore di cento")
        else:
            print("Il numero è minore di 100")
    else:
        print("Il numero è dispari")
elif x < 0:
    print("Il numero è negativo")
else:
    print("Il numero è uguale a zero")
