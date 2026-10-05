#Scrivi un programma che calcoli quante fette di pizza riceve
# ogni persona e quante fette avanzano. Il programma deve:
# 1. Chiedere all'utente di inserire il numero di persone
# 2. Chiedere all'utente di inserire il numero di pizze disponibili
# 3. Calcolare il numero di fette di pizza disponibili
# 4. Calcolare quante fete riceve ogni persona
# 5. Calcolare quante fette avanzano
# 6. Stampare il numero di fette per persona e le fette avanzate
SLICE_PER_PIZZA = 8

people = int(input("Inserire il numero di persone:"))
pizza = int(input("Inserire il numero di pizze:"))

pizza_slice = pizza * SLICE_PER_PIZZA
slice_person = pizza_slice // people
leftover_slice = pizza_slice % people

print("Il numero di fette per persona è di:", slice_person,", mentre il numero di fette avanzate è di:", leftover_slice)
