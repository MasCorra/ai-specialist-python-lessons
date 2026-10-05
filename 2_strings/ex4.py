#Scrivi un programma che estragga le informazioni da un codice prodotto.
# Il programma deve:
# 1. Chiedere all'utente di inserire un codice prodotto (IT-2026-PANE-0045)
# 2. Estrarre e stampare il codice del paese
# 3. Estrarre e stampare l'anno
# 4. Estrarre e stampare il nome del prodotto in minuscolo
# 5. Estrarre il numero del lotto, convertirlo in un numero intero e stamparlo.
# 6. Stampare la posizione in cui compare la prima volta il carattere "-".
SEPARATOR="-"
codice_prodotto= input("Inserire un codice prodotto: ").strip()
country_index = codice_prodotto.find(SEPARATOR)
print("Il codice del paese è:", codice_prodotto[:country_index])

codice_sliced_prodotto = codice_prodotto[country_index+1:]
year_index = codice_sliced_prodotto.find(SEPARATOR)
print("Il codice dell'anno è:", codice_sliced_prodotto[:year_index])

codice_sliced2_prodotto = codice_sliced_prodotto[year_index+1:]
name_index = codice_sliced2_prodotto.find(SEPARATOR)
print("Il codice dell prodotto è:", codice_sliced2_prodotto[:name_index].lower())

lotto_index = codice_prodotto.rfind("-")
print("Il codice del lotto è:", int(codice_prodotto[lotto_index+1:]))
print("il primo - compare in posizione:",country_index)
