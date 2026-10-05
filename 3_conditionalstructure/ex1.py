# Chiedere all'utente di inserire il proprio indirizzo email
# Rimuovere eventuali spazi e convertire l'email tutta in maiuscola
# Se la email contiene il carattere @, estrarre e stampare il nome utente e il dominio
# Altrimenti, stampare "Email non valida"

email = input("Inserire la propria email: ").strip().lower().replace(" ","")


if "@" in email:
    email_index = email.find("@")
    username = email[:email_index]
    domain = email[email_index+1:]
    print("Email valida!", username, domain)

else:
    print("Email non valida!")