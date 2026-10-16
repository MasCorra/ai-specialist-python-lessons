# Definisci una lista con quattro temperature, anche negative.
# Calcola media, valore minimo e massimo.
# Se la media è sotto zero stampa "Giornata gelida";
# se è tra zero incluso e 20 escluso, "Giornata fresca";
# altrimenti "Giornata calda". Stampa anche l’escursione termica.

try:
    temp1= int(input("Inserire la prima temperatura: "))
    temp2= int(input("Inserire la seconda temperatura: "))
    temp3= int(input("Inserire la terza temperatura: "))
    temp4= int(input("Inserire la quarta temperatura: "))
except ValueError as error:
    print("errore di valore: il valore inserito non è valido!")
    print(error)
else:
    temperature = [temp1 , temp2 , temp3 , temp4]
    media= sum(temperature)/len(temperature)
    if media < 0:
        print("Giornata Gelida")
    elif 20 > media >= 0:
        print("Giornata Fresca")
    else:
        print("Giornata Calda")
    escursione= max(temperature) - min(temperature)
    print("La temperatura massima è di:", max(temperature), '°C')
    print("La temperatura minima è di:", min(temperature), '°C')
    print("La temperatura media è di:", media, '°C')
    print("C'è un escursione termica di:", escursione, "°C")
