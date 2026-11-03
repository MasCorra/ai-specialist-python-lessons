# Scrivi un programma che cifra un messaggio con il cifrario di Cesare. Il programma deve:
# 1. Definire una funzione “cifra_lettera” che riceve una lettera e uno spostamento e restituisce
# la lettera cifrata, preservando maiuscole/minuscole e lasciando invariati spazi e caratteri non alfabetici
# 2. Definire una funzione “cifra_messaggio” che riceve un testo e uno spostamento e applica “cifra_lettera” a
# ogni carattere del testo con un ciclo, costruendo il messaggio cifrato
# 3. Chiedere all’utente di inserire un messaggio e uno spostamento numerico
# 4. Chiamare “cifra_messaggio” e stampare il messaggio cifrato
# 5. Decifrare il messaggio cifrato applicando lo spostamento inverso e verificare che il risultato coincida con
# il messaggio originale
import sys

alfabeto_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z"]
alfabeto_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]


def cifra_lettera(lettera, cifra):
    if lettera in alfabeto_lower:
        index_lettera = alfabeto_lower.index(lettera)
        index_lettera = (index_lettera + cifra) % len(alfabeto_lower)
        return alfabeto_lower[index_lettera]
    elif lettera in alfabeto_upper:
        index_lettera = alfabeto_upper.index(lettera)
        index_lettera = (index_lettera + cifra) % len(alfabeto_upper)
        return alfabeto_upper[index_lettera]
    else:
        return lettera


def cifra_messaggio(testo, spostamento):
    testo_cifrato = ""
    if testo is (None or ""):
        print('Il testo inserito è vuoto')
        return None
    else:
        for lettera in testo:
            testo_cifrato = testo_cifrato + cifra_lettera(lettera, spostamento)
        return testo_cifrato

messaggio = input("Inserire un messaggio da cifrare: ")
try:
    numero = int(input("Inserire una chiave numerica: "))
except ValueError as errore:
    print("Non hai inserito una chiave valida")
    print(errore)
    sys.exit()
else:
    messaggio_cifrato = cifra_messaggio(messaggio, numero)
    print(messaggio_cifrato)