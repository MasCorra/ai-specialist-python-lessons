#Scrivi un programma che analizza una frase inserita dall'utente. Il programma deve:
# 1. Chiedere all'utente di inserire una frase
# 2. Contare e stampare il numero totale di caratteri inclusi gli spazi
# 3. Contare e stampare il numero di vocali
# 4. Verificare e stampare se la frase contiene la parola "Python"
# 5. Estrarre e stampare la prima e l'ultima parola della frase
# 6. Sostituire tutte le vocali "a" con il carattere "*" e stampare il risultato

frase = input("Inserire una frase a piacere:")

print("Il numero di caratteri inseriti è:", len(frase))

vowel_count = frase.count("a") + frase.count("e") + frase.count("i") + frase.count("o") + frase.count("u")
print("Il numero di vocali è:", vowel_count)

bool = "Python" in frase.title()
print("La parola Python è presente nella frase?", bool)

first_index = frase.find(" ")
last_index = frase.rfind(" ")
first = frase[:first_index]
last = frase[last_index+1:]
print("La prima parola è:", first)
print("L'ultima parola è:", last)
frase_sub = frase.replace("a", "*")