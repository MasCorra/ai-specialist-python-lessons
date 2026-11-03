# Scrivi un programma che calcola le statistiche di una partita di basket. Il programma deve:
# 1. Chiedere quanti giocatori hanno segnato nel quarto
# 2. Per ogni giocatore, inserire nome, punti segnati, rimbalzi e assist in un dizionario e aggiungere
# ogni dizionario a una lista
# 3. Definire una funzione “miglior_marcatore” che riceve la lista e restituisce il giocatore con più punti
# 4. Definire una funzione “statistiche_squadra” che riceve la lista e restituisce un dizionario con:
# punti totali, rimbalzi totali, assist totali e medie per giocatore
# 5. Usare un ciclo per ottenere i nomi dei giocatori con più di 10 punti
# 6. Stampare le statistiche della squadra, il miglior marcatore e i giocatori

def miglior_marcatore(lista):
    massimo_punti = 0
    miglior_giocatore = None
    for player in lista:
        if player["Punti"] > massimo_punti:
            massimo_punti = player["Punti"]
            miglior_giocatore = player
    return miglior_giocatore

def statistiche_squadra(lista):
    statistiche_partita: dict[str, int | float ] = {"Punti Totali" : 0, "Rimbalzi Totali" : 0, "Assist Totali" : 0,
                                                    "Media Punti": 0, "Media Rimbalzi": 0, "Media Assist": 0}
    for player in lista:
        statistiche_partita["Punti Totali"] += player["Punti"]
        statistiche_partita["Rimbalzi Totali"] += player["Rimbalzi"]
        statistiche_partita["Assist Totali"] += player["Assist"]
    punti_totali = statistiche_partita["Punti Totali"]
    rimbalzi_totali = statistiche_partita["Rimbalzi Totali"]
    assist_totali = statistiche_partita["Assist Totali"]
    if len(lista) > 0:
        statistiche_partita["Media Punti"] = punti_totali / len(lista)
        statistiche_partita["Media Rimbalzi"] = rimbalzi_totali / len(lista)
        statistiche_partita["Media Assist"] = assist_totali / len(lista)
    return statistiche_partita

try:
    numero_giocatori = int(input("Inserire numero giocatori che hanno segnato: "))
except ValueError as e:
    print(e)
else:
    lista_statistiche = []
    for i in range (numero_giocatori):
        statistiche_giocatori = {"Nome": input(f"Inserire il nome del {i + 1}° giocatore: "),
                                 "Punti": int(input(f"Inserire il numero di punti del {i + 1}° giocatore: ")),
                                 "Rimbalzi": int(input(f"Inserire numero di rimbalzi del {i + 1}° giocatore: ")),
                                 "Assist": int(input(f"Inserire numero assist del {i + 1}° giocatore: "))}
        lista_statistiche.append(statistiche_giocatori)
    giocatori_dieci = []
    for giocatore in lista_statistiche:
        if giocatore["Punti"] > 10:
            giocatori_dieci.append(giocatore["Nome"])

    statistiche = statistiche_squadra(lista_statistiche)
#PRINT STATISTICHE
    for chiave, valore in statistiche.items():
        print(f"{chiave:<15}: {valore}")
    print("-" * 30)
    print(f"{'Nome':<15} {'Punti':>8} {'Rimbalzi':>10} {'Assist':>8}")
    print("-" * 45)
    giocatore = miglior_marcatore(lista_statistiche)
    print(f"{giocatore['Nome']:<15} "
          f"{giocatore['Punti']:>8} "
          f"{giocatore['Rimbalzi']:>10} "
          f"{giocatore['Assist']:>8}")
    print("-" * 45)
    print("Giocatori con piu di 10 punti: ", ", ".join(giocatori_dieci))







