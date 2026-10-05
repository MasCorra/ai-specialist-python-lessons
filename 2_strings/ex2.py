# Scrivi un proigramma che data un stringa contenente un indirizzo mail,
# mostri diverse informazioni. Il programma deve:
# 1. Chiedere all'utente di inserire una stringa contenente un indirizzo email
# 2. Estrarre e stampare il nome utente (parte prima di @)
# 3. Estrarre e stampare il dominio
# 4. Contare e stampare il numero di volte in cui appare il carattere "a"
# 5. Creare e stampare l'email con il nome utente tutto maiuscolo e il dominio tutto minuscolo

email= input("Inserire l'indirizzo email: ").strip().lower()

part = email[:email.find("@")]
print("Il nome utente è:", part)

part2 = email[email.find("@")+1:]
print("Il dominio è:", part2)

count = email.count("a")
print("Il carattere a è ripetuto", count, "volte")


formatted_email =f"{part.upper()}@{part2}"
print("Email formattata:", formatted_email)


