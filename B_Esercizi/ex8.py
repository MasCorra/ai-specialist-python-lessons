# Scrivi un programma che analizza i dati di migrazione di uno stormo di uccelli. Il programma deve:
# 1. Chiedere quanti giorni di migrazione tracciare; per ogni giorno inserire:
# distanza percorsa (km), direzione (N/S/E/O) e temperatura (°C), memorizzando ogni giorno come dizionario in una lista
# 2. Definire una funzione “statistiche_migrazione” che riceve la lista e restituisce un dizionario con:
# distanza totale, distanza media, giorno con la tappa più lunga
# 3. Definire una funzione “media_per_direzione” che riceve la lista e restituisce un dizionario
# {direzione: distanza_media} calcolando la media delle distanze per ogni direzione
# 4. Usare un ciclo per identificare i “giorni critici”: temperatura sotto 5°C e distanza superiore a 100 km
# 5. Chiamare entrambe le funzioni e stampare le statistiche generali
# 6. Stampare la distanza media per ogni direzione
# 7. Stampare i giorni critici con tutti i loro dati; se non ce ne sono, stampare “Nessun giorno critico rilevato”

def statistiche_migrazione(lista):
    distanza_totale = 0
    tappa_lunga = 0
    giorno_tappa= 0
    for percorso in lista:
        distanza_totale += int(percorso["Distanza Percorsa"])
        if percorso["Distanza Percorsa"] > tappa_lunga:
            tappa_lunga = int(percorso["Distanza Percorsa"])
            giorno_tappa = percorso["Giorno"]
    distanza_media = distanza_totale / len(lista)
    stat_migrazione = {
        "Distanza Totale": distanza_totale,
        "Distanza Media": distanza_media,
        "Tappa Piu Lunga": tappa_lunga,
        "Giorno Tappa Lunga": giorno_tappa
    }
    return stat_migrazione

def media_per_direzione(lista):
    direzione_nord = 0
    count_nord = 0
    direzione_sud = 0
    count_sud = 0
    direzione_est = 0
    count_est = 0
    direzione_ovest = 0
    count_ovest = 0
    direzione_nd = 0
    count_nd = 0
    for percorso in lista:
        if percorso["Direzione"] == "N":
            direzione_nord += percorso["Distanza Percorsa"]
            count_nord += 1
        elif percorso["Direzione"] == "S":
            direzione_sud += percorso["Distanza Percorsa"]
            count_sud += 1
        elif percorso["Direzione"] == "E":
            direzione_est += percorso["Distanza Percorsa"]
            count_est += 1
        elif percorso["Direzione"] == "O":
            direzione_ovest += percorso["Distanza Percorsa"]
            count_ovest += 1
        else:
            direzione_nd += percorso["Distanza Percorsa"]
            count_nd += 1

    medie_direzioni= {
        "Media direzione N": direzione_nord / count_nord ,
        "Media direzione S": direzione_sud / count_sud,
        "Media direzione E": direzione_est / count_est,
        "Media direzione O": direzione_ovest / count_ovest

    }

try:
    giorni = int(input("Inserire il numero di giorni da tracciare: "))
except ValueError as e:
    print(e)
    exit()
else:
    dati_giornalieri = {"Giorno": 0 , "Distanza Percorsa": 0 , "Direzione": "", "Temperatura": None}
    giorni_migrazione = []
    for giorno in range(giorni):
        dati_giornalieri = {
            "Giorno": giorno + 1,
            "Distanza Percorsa": int(input(f"Inserire la distanza percorsa il {giorno +1}° giorno in km: ")),
            "Direzione": input(f"Inserire la direzione intrapresa il {giorno +1}° giorno (N/S/E/O): "),
            "Temperatura": int(input(f"Inserire la temperatura del {giorno +1}° giorno in °C: "))
        }
        giorni_migrazione.append(dati_giornalieri)
    giorni_critici = []
    for giorno in giorni_migrazione:
        if giorno["Temperatura"] <= 5 and giorno["Distanza Percorsa"] > 100:
            giorni_critici.append(giorno)






