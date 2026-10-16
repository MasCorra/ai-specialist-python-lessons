# Hai 27 adesivi, 19 penne e 24 cartellini.
# Chiedi quanti kit identici si vogliono preparare.
# Ogni kit richiede 2 adesivi, 1 penna e 3 cartellini.
# Se il numero inserito è positivo, verifica se tutti i materiali bastano.
# Se bastano, stampa gli avanzi dei tre materiali;
# se non bastano, indica per ciascun materiale quanti pezzi mancano (zero se già sufficiente).
# Gestisci input non numerici.
ADESIVI = 27
PENNE = 19
CARTELLINI = 24
try:
    kit = int(input("Inserire il numero di kit "))
except ValueError as error:
    print("Errore, non hai inserito un numero intero")
    print(error)
else:
    if kit < 0:
        print("Hai inserito un numero negativo")

    else:
        adesivi = kit*2
        penne = kit
        cartellini = kit * 3
        if adesivi <= ADESIVI and penne <= PENNE and cartellini <= CARTELLINI:
            print("Avanzano:",ADESIVI - adesivi, "adesivi,", PENNE - penne ,"penne,", CARTELLINI - cartellini ,"cartellini")
        if adesivi > ADESIVI:
            print("Mancano:",adesivi - ADESIVI, "adesivi")
        if penne > PENNE:
            print("Mancano:", penne - PENNE, "penne")
        if cartellini > CARTELLINI:
            print("Mancano:", cartellini - CARTELLINI, "cartellini")