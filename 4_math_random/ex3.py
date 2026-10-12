# Scrivi un programma che aiuti a calcolare il materiale per piastrellare
# il pavimento di una stanza quadrata.
# Il programma deve:
# 1. Definire una costante con il lato di una piastrella in metri (0.30)
# 2. Definire una costante con il numero di piastrelle contenute in una scatola (12)
# 3. Definire una costante con il prezzo di una scatola di piastrelle (30)
# 4. Chiedere all'utente di inserire la superficie della stanza in metri quadrati
# 5. Convertire la superficie in un numero decimale
# 6. Calcolare e stampare la lunghezza del lato della stanza, arrotondata a due cifre decimali
# 7. Calcolare e stampare quante piastrelle intere entrano lungo un lato senza doverle tagliare
# 8. Calcolare e stampare quante piastrelle servono in totale per coprire tutto il pavimento,
# considerando che ogni piastrella tagliata va comprata intera
# 9. Calcolare e stampare quante scatole bisogna acquistare
# 10. Calcolare e stampare la spesa totale
# 11. Se le piastrelle avanzate sono più di 5, stampare "Avanzeranno diverse piastrelle",
# altrimenti stampare "Avanzeranno poche piastrelle"
import math

LATO_PIASTRELLA = 0.30
PIASTRELLE_SCATOLA = 12
COSTO_SCATOLA= 30

metri_quadri = float(input("Inserire i metri quadri: "))
lato_stanza = math.sqrt(metri_quadri)
round_lato = round(lato_stanza,2)
print("Il lato della stanza è di:", round_lato, "metri")
##print(f"Il lato della stanza è di {lato_stanza:.2f}")
num_piastrelle_lato= round_lato // LATO_PIASTRELLA
print("Lungo un lato entrano:", num_piastrelle_lato,"piastrelle intere")
remain_piastrelle = round_lato % LATO_PIASTRELLA
if not remain_piastrelle:
    tot_piastrelle = num_piastrelle_lato ** 2
else:
    tot_piastrelle = (num_piastrelle_lato + 1) ** 2
print("Bisogna acquistare", tot_piastrelle,"piastrelle")
tot_scatole = math.ceil(tot_piastrelle /PIASTRELLE_SCATOLA)
spesa_totale = tot_scatole * COSTO_SCATOLA
print(f"La spesa totale è di", spesa_totale,"€")
piastrelle_comprate= tot_scatole * PIASTRELLE_SCATOLA
avanzi_piastrelle = piastrelle_comprate - tot_piastrelle

if avanzi_piastrelle > 5:
    print("Avanzeranno diverse piastrelle")
else:
    print("Avanzeranno poche piastrelle")

print("Avanzano esattamente:", avanzi_piastrelle,"piastrelle")


