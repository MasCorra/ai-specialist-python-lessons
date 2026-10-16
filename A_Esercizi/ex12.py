# Le distanze tra quattro tappe consecutive sono [3, 7, 4, 6] km.
# Chiedi il massimo numero di km percorribili.
# Se il valore è valido, stabilisci quante delle prime tappe consecutive possono essere completate
# senza superare il limite.
# Non usare cicli: confronta le somme progressive delle prime una, due, tre e quattro tratte

distanze = [2, 7, 4, 6]
try:
    massimo = int(input("Inserire i km percorribili: "))
except ValueError as error:
    print("Il valore inserito non è valido")
    print(error)
else:
    print(distanze)
    if massimo >= distanze[0]:
        if massimo >= sum(distanze[0:2]):
            if massimo >= sum(distanze[0:3]):
                if massimo >= sum(distanze[0:4]):
                    print("Riuscirai a percorrere tutte le tappe")
                else:
                    print("Riuscirai a percorrere tre tappe")
            else:
                print("Riuscirai a percorrere due tappe")
        else:
            print("Riuscirai a percorrere una tappa")
    else:
        print("Non riuscirai a percorrere alcuna tappa")

