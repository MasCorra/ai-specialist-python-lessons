# Una fila di posti è rappresentata dalla lista
# ["libero", "occupato", "libero", "occupato", "libero"].
# Chiedi un numero di posto da 1 a 5.
# Se il numero è valido e il posto è libero,
# cambia il valore in "occupato".
# Negli altri casi stampa una spiegazione.
# Alla fine mostra la lista e quanti posti liberi restano.

lista= ['libero', 'occupato', 'libero', 'occupato', 'libero']
try:
    posto = int(input('Inserire un posto da 1 a 5: '))
except ValueError as error:
    print("errore di valore: il valore inserito non è valido!")
    print(error)
else:
    if 1 <= posto <= 5:
        if lista[posto-1]=='libero':
            lista[posto-1]='occupato'
        else:
            print('Il posto era occupato')
    else:
        print('Il posto inserito non è valido')

    print(lista)
    liberi=lista.count('libero')
    print('Ci sono ancora',liberi,'posti liberi')
