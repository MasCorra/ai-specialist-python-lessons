# Parti dalla lista ["Anna", "Bruno", "Carla", "Diego"].
# Chiedi il nome di una persona da mettere in testa ai turni.
# Se è già presente, rimuovila dalla posizione originale;
# in ogni caso inseriscila in prima posizione.
# Stampa chi è primo, chi è ultimo e l’ordine completo.
# Tratta i nomi con iniziale maiuscola.

lista = ["Anna", "Bruno", "Carla", "Diego"]
nome = input("Inserire una persona da mettere in testa ai turni: ").strip().title()
if not nome:
    print('Devi inserire un nome valido')
else:
    try:
        presenza = lista.index(nome)
    except ValueError as error:
        print("Il nome inserito non è presente nella lista")
        print(error)
    else:
        lista.remove(nome)
    finally:
        lista.insert(0 , nome)
        print('Il primo in lista è:',lista[0])
        print('L\'ultimo in lista è:', lista[-1])
        print(lista)

