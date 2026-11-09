# Scrivi un programma che gestisce un file JSON con informazioni sulle pizze.
# Il programma deve:
# 1. Creare un file JSON con una lista di 3 pizze, ognuna con nome e prezzo
# 2. Leggere il file JSON e caricare i dati in una variabile
# 3. Stampare tutte le pizze con i loro prezzi
# 4. Calcolare e stampare il prezzo medio delle pizze
# 5. Aggiungere una nuova pizza alla lista chiedendo i dati all'utente
# 6. Salvare le pizze nel file JSON
import json
def main():
    with open('pizze.json', 'r', encoding="utf-8") as file:
        pizzas= json.load(file)

    print(pizzas)
    total_price=0
    for pizza in pizzas:
        print(f"Pizza {pizza["name"]}:{pizza["price"]} €")
        total_price+=pizza["price"]

    average_price=total_price/len(pizzas)
    print(f"Average price: {average_price:.2f} €")

    name = input("Inserire nome pizza nuova")
    prezzo = float(input("Inserire nome pizza nuova"))

    pizzas.append({"name": name, "price": prezzo})
    with open('pizze.json', 'w', encoding="utf-8") as file:
        json.dump(pizzas, file, indent=4,ensure_ascii=False)
if __name__ == "__main__":
    main()