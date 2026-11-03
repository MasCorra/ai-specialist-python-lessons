# Scrivi un programma che gestisce il log di comunicazioni di una stazione spaziale. Il programma deve:
# 1. Chiedere quanti messaggi inserire; per ognuno raccogliere tramite ciclo: timestamp (es. "14:32"),
#    mittente, priorità (1=Alta, 2=Media, 3=Bassa) e testo, e memorizzare ogni messaggio come dizionario in una lista
# 2. Definire una funzione "filtra_per_priorita" che riceve la lista e una priorità e
#    restituisce tutti i messaggi con quella priorità
# 3. Definire una funzione "messaggi_per_mittente" che riceve la lista e restituisce un dizionario {mittente: numero_di_messaggi}
# 4. Usare un ciclo per estrarre solo i testi dei messaggi ad alta priorità (1) e stamparli con timestamp e mittente
# 5. Chiedere all'utente una priorità da filtrare, chiamare "filtra_per_priorita" e stampare i messaggi trovati
# 6. Chiamare "messaggi_per_mittente" e stampare quanti messaggi ha inviato ogni mittente