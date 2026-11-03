#Scrivi un programma che gestisce un dizionario di frequenze radio. Il programma deve:
# 1. Creare un dizionario con almeno 5 stazioni radio come chiavi e le loro frequenze FM come valori.
# 2. Stampare tutte le stazioni disponibili e le loro frequenze
# 3. Chiedere all’utente di inserire il nome di una stazione
# 4. Se la stazione esiste, stampare la sua frequenza
# 5. Se non esiste, stampare un messaggio di errore
# 6. Chiedere all’utente se vuole aggiungere la nuova stazione: se sì,
# chiedere la frequenza e aggiungerla al dizionario, poi stampare il dizionario aggiornato

def stampa_dizionario(dizionario):
    if not dizionario:
        print("Il dizionario è vuoto.")
        return

    larghezza = max(len(chiave) for chiave in dizionario)

    for chiave, valore in dizionario.items():
        print(f"{chiave:<{larghezza}} : {valore}")

stazioni_radio = {
    "RTL 102.5": 102.5,
    "Radio Deejay": 99.7,
    "RDS": 100.0,
    "Radio 105": 105.0,
    "Virgin Radio": 104.5,
    "Radio Italia": 106.7,
    "Radio Capital": 90.0
}

stampa_dizionario(stazioni_radio)
stazione_richiesta: str = input("Inserire la stazione richiesta: ").title()
frequenza: float | int
for radio, frequenza in stazioni_radio.items():
    if stazione_richiesta == radio:
        print(f"{radio}: {frequenza} MHz")
        break
else:
    print("Errore, la stazione richiesta non esiste")
    while True:
        risposta = input("Vuoi aggiungere la stazione? (si/no): ").strip().lower()

        if risposta in ("si", "sì", "no"):
            break

        print("Risposta non valida. Inserisci si o no.")

    if risposta in ("si", "sì"):
        try:
            frequenza_richiesta = float(input("Inserire la frequenza della stazione: "))
        except ValueError as e:
            print(e)
        else:
            stazioni_radio[stazione_richiesta] = frequenza_richiesta
            stampa_dizionario(stazioni_radio)




