# Scrivi un programma che valuta se uno studente ha superato l'anno scolastico. Il programma deve:
# 1. Chiedere all'utente di inserire la media dei voti dello studente
# 2. Chiedere all'utente di inserire la percentuale di presenza
# 3. Chiedere all'utente se lo studente ha partecipato a progetti extra (sì/no)
# 4. Determinare la media minima richiesta (6 normalmente, 5.5 se ha partecipato a progetti extra)
# 5. Verificare se la media è sufficiente e la presenza è almeno del 75%
# 6. Stampare se lo studente ha superato l'anno scolastico oppure no

media_voti = float(input("Inserire la media dei voti: "))
percent_presenze = float(input("Inserire la percentuale di presenze: "))
proj_extra= input("Hai partecipato a progetti extra? (si/no) ")

if proj_extra == 'si':
    if media_voti >= 5.5:
        if percent_presenze >= 0.75:
            print("Promosso")
        else:
            print("Bocciato")
    else:
        print("Bocciato")
else:
    if media_voti >= 6:
        if percent_presenze >= 0.75:
            print("Promosso")
        else:
            print("Bocciato")
    else:
        print("Bocciato")

