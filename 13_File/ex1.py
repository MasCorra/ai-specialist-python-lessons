# Scrivi un programma che legge un file di testo e conta quante righe
# contiene. Il programma deve:
# 1. Chiedere all'utente il nome del file da leggere
# 2. Aprire il file in modalità lettura
# 3. Leggere tutte le righe del file e contarle
# 4. Chiudere il file
# 5. Stampare il numero totale di righe trovate
# 6. Gestire il caso in cui il file non esista mostrando un messaggio di errore
def main():
    nome_file = input("Inserire il nome del file da aprire: ")

    try:
        file = open(nome_file, "r")
    except FileNotFoundError:
        print(f"File {nome_file} non trovato")
    else:
        file_lines = file.readlines()
        count_lines = len(file_lines)

        file.close()
        print(f"Il fine contiene {count_lines} linee")

if __name__ == "__main__":
    main()