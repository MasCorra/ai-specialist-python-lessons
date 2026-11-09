# Scrivi un programma che registri le ore lavorate da un dipendente.
# Il programma deve:
# 1. Chiedere all'utente la data e il numero di ore lavorate in quel giorno
# 2. Salvare i dati su una nuova riga del file "ore.txt", separando la data e le ore con
# il carattere "," (es. 06/11/2026,8)
# 3. Aprire il file in lettura e, usando un ciclo, dividere ogni riga nella data e nelle ore
# 4. Convertire le ore in un numero decimale e calcolare il totale delle ore lavorate
# 5. Stampare ogni giorno con le relative ore
# 6. Definire una costante con la paga oraria e stampare il compenso totale
# 7. Se il totale delle ore supera 160, stampare "Sono presenti ore di straordinario" e quante sono
PAGA_ORARIA = 8
SOGLIA_ORE = 160

def main():
    data= input("Inserire la data: ")
    try:
        ore = float(input("Inserire la ore lavorate: "))
    except ValueError as e:
        print("Inserire un numero valido")
        return

    try:
        with open("registro.txt", "x") as file:
            file.write("")
    except FileExistsError:
        ...
    with open("registro.txt", "r") as file:
        lines = file.readlines()
    lines.append(data + "," + str(ore) + "\n")

    with open("registro.txt", "w") as file:
        file.writelines(lines)
    print(lines)

    ore_totali = 0
    for line in lines:
        #index = line.find(",")
        #data_linea = line[:index]
        #ore_linea= float(line[index + 1:])
        #ore_totali += ore_linea
        parts=line.split(",")
        data_linea = parts[0]
        ore_linea = parts[1]
        ore_totali += float(ore_linea)

        print(f"{data_linea} - {ore_linea}")


    salario = ore_totali * PAGA_ORARIA
    print(f"Totale importo stipendio: {salario:.2f}")
    print(f"Totale ore lavorate: {ore_totali:.2f}")

    if ore_totali > SOGLIA_ORE:
        print("Sono presenti ore di straordinario!")

        ore_extra= ore_totali - SOGLIA_ORE
        print(f"Totale ore straordinario: {ore_extra:.2f}")


if __name__ == "__main__":
    main()