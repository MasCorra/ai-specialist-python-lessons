#Scrivi un programma che analizza i dati di velocità di un corridore su pista. Il programma deve:
# 1. Chiedere all’utente quanti giri ha percorso il corridore
# 2. Inserire in una lista il tempo in secondi di ogni giro tramite un ciclo
# 3. Calcolare con un ciclo la lista delle velocità in km/h (ogni giro è di 400 metri: velocità = 0.4 / tempo * 3600)
# 4. Stampare ogni giro con il relativo tempo e velocità formattata a 2 decimali
# 5. Stampare la velocità media, quella massima e quella minima
# 6. Indicare quale giro è stato il più veloce e quale il più lento
import sys

try:
    giri = int(input("Inserire il numero di giri fatti: "))
except ValueError as e:
    print(e)
    sys.exit()
else:
    tempi = [float(input(f"Inserire il tempo impiegato per il {i}° giro: ")) for i in range(1, giri + 1)]
    velocita = [0.4 / t * 3600 for t in tempi]
for i,j,k  in zip(range(1,giri+1),velocita, tempi):
    print(f"Giro {i}: completato in {k} s alla velocita di {j:.2f} km/h")

print(f"La velocità media è di: {sum(velocita)/len(velocita):.2f} km/h")
print(f"La velocità massima è di: {max(velocita):.2f} km/h del {velocita.index(max(velocita))+1}° giro")
print(f"La velocità minima è di: {min(velocita):.2f} km/h del {velocita.index(min(velocita))+1}° giro")


