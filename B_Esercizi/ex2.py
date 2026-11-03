#Scrivi un programma che calcola quante volte una base azotata appare in una sequenza di DNA. Il programma deve:
# 1. Chiedere all’utente di inserire una sequenza di basi (es. “ATCGGTA”)
# 2. Convertire la sequenza in maiuscolo
# 3. Verificare che la sequenza contenga solo i caratteri A, T, C, G;
# se contiene caratteri non validi stampare un messaggio di errore e terminare
# 4. Chiedere all’utente quale base vuole cercare (A, T, C o G)
# 5. Contare quante volte quella base appare nella sequenza
# 6. Stampare il risultato e la percentuale rispetto alla lunghezza totale della sequenza
import sys
sequenza = input("Inserire una sequenza di basi azotate: ").upper().strip()

for val in sequenza:
    if val != "A" and val != "T" and val != "C" and val != "G":
        print("ERRORE: la sequenza inserita non è valida")
        sys.exit()

base=input("Inserire una base: ").upper().strip()
if base != "A" and base != "T" and base != "C" and base != "G":
    print("ERRORE: il valore inserito non è una base")
    sys.exit()

contatore = 0
for val in sequenza:
    if val == base:
        contatore += 1
print("Ci sono ", contatore,"basi", base, "la percentuale è di:", contatore/len(sequenza)*100, "%")
