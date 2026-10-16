# Scrivi un programma Python che conta quante vocali sono presenti in una stringa di testo.
# Il programma deve:
# 1. Chiedere all'utente un testo da analizzare
# 2. Identificare tutte le vocali (sia minuscole che maiuscole) presenti nella stringa
# 3. Visualizzare ogni vocale trovata
# 4. Contare il numero totale di vocali
# 5. Visualizzare il risultato finale

testo= input("Inserire un testo da analizzare")
vocali = ['a','e','i','o','u']
counter=0
for i in testo:
    if i.lower() in vocali:
        print(i)
        counter+=1
print('conta_vocali', counter)