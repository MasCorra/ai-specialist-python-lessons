# Scrivi un programma che utilizza le list comprehension per filtrare
# e trasformare una lista di numeri. Il programma deve:
#
# 1. Creare una lista con i numeri da 1 a 20
# 2. Utilizzare una list comprehension per creare una lista con solo
# i numeri pari dalla lista originale
# 3. Utilizzare una list comprehension per creare una lista con i quadrati
# di tutti i numeri dalla lista originale
# 4. Utilizzare una list comprehension per creare una lista con i quadrati
# dei numeri dispari maggiori di 10 dalla lista originale
# 5. Stampare tutte le liste create

# lista_numeri = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lista_numeri=list(range(1,21))
lista_pari = [x for x in lista_numeri if x%2==0]
#print(lista_pari)
lista_quadrati = [x**2 for x in lista_numeri]
#print(lista_quadrati)
lista_speciale = [x**2 for x in lista_numeri if x >10 and x%2!=0]
#print(lista_speciale)
print('numeri:', ', '.join(str(x) for x in lista_numeri))
print('numeri pari:', ', '.join(str(x) for x in lista_pari))
print('numeri quadrati:', ', '.join(str(x) for x in lista_quadrati))
print('numeri speciali:', ', '.join(str(x) for x in lista_speciale))
