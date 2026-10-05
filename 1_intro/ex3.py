# Scrivi un programma che calcoli l'area e il perimetro di un rettangolo. il programma deve:
# 1. Chiedere all'utente di inserire la base del rettangolo.
# 2. Chiedere all'utente di iserire l'altezza del rettangolo.
# 3. Calcolare l'area del rettangolo
# 4. Calcolare il perimetro del rettangolo
# 5. Stampare il valore dell'area
# 6. Stampare il valore del perimetro.

base = float(input("Inserisci il valore della base:"))
altezza = float(input("Inserisci il valore dell'altezza:"))
area = base * altezza
perimetro = 2* (base + altezza)
print("L'area del rettangolo è di:", area)
print("Il perimetro del rettangolo è di:", perimetro)