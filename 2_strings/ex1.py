# Scrivi un programma che manipoli una stringa contenente il nome
# completo di una persona. Il programma deve:
# 1. Chiedere in input all'utente un nome completo.
# 2. Convertire e stampare il nome con tutte le lettere maiuscole
# 3. Convertire e stanmpare il nome con tutte le lettere minuscole
# 4. Convertire e stampare il nome con la prima lettera di ogni parola maiuscola
# 5. Contare e stampare il numero totale di caratteri
# 6. Sostituire gli spazi con il trattino basso e stampare il risultato.

full_name = input("Inserire nome e cognome:")
upper_name = full_name.upper()
print("upper():", upper_name)

lower_name = full_name.lower()
print("lover():", lower_name)

title_name = full_name.title()
print("title():", title_name)

number_name= len(full_name)
print("number():", number_name)

underscore_name = full_name.replace(" ", "_")
print("replace():", underscore_name)

numb = len(full_name.replace(" ", ""))

